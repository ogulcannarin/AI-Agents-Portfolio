"""OpenAI chat completions + tool-calling döngüsü."""
import json

from openai import OpenAI

from ai_assistant.config import get_api_key, get_model
from ai_assistant.tools.schema import DISPATCH, TOOLS

SYSTEM_PROMPT = (
    "Sen, terminalde çalışan bir AI Coding Assistant'sın. Kullanıcının projesi "
    "üzerinde çalışıyorsun. Dosyaları görmek için list_files ve read_file "
    "araçlarını kullan; varsayımda bulunmak yerine önce dosyayı oku. Bir dosyayı "
    "değiştirmek istediğinde write_file aracını çağır (kullanıcıya diff gösterilip "
    "onay istenecek). Komut çalıştırman gerekiyorsa run_command kullan (kullanıcıya "
    "onay sorulacak). Git değişikliklerini incelemek için git_diff kullan (salt "
    "okunur). Commit atman istendiğinde önce mutlaka git_diff ile değişiklikleri "
    "incele, sonra Conventional Commits formatında (fix:/feat:/refactor:/docs:/"
    "test:) kısa ve açıklayıcı bir mesajla git_commit aracını çağır (kullanıcıya "
    "onay sorulacak) — asla run_command ile doğrudan 'git commit' çalıştırma. "
    "Kullanıcıyla Türkçe konuş."
)

MAX_TOOL_ITERATIONS = 15


class Assistant:
    def __init__(self):
        self.client = OpenAI(api_key=get_api_key())
        self.model = get_model()
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def send(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})

        for _ in range(MAX_TOOL_ITERATIONS):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=TOOLS,
            )
            message = response.choices[0].message
            self.messages.append(message.model_dump(exclude_none=True))

            if not message.tool_calls:
                return message.content or ""

            for tool_call in message.tool_calls:
                result = self._execute_tool(tool_call)
                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )

        return (
            "Çok fazla ardışık araç çağrısı yapıldı, işlemi durduruyorum. "
            "Lütfen isteğinizi daha küçük adımlara bölün."
        )

    @staticmethod
    def _execute_tool(tool_call) -> str:
        name = tool_call.function.name
        handler = DISPATCH.get(name)
        if handler is None:
            return f"Hata: bilinmeyen araç '{name}'."
        try:
            args = json.loads(tool_call.function.arguments or "{}")
        except json.JSONDecodeError:
            return "Hata: araç argümanları çözümlenemedi."
        try:
            return handler(args)
        except Exception as exc:  # noqa: BLE001 - araç hatası modele bildirilir
            return f"Hata: araç çalıştırılırken bir istisna oluştu: {exc}"
