"""Terminal REPL giriş noktası."""
from typing import Optional

from rich.console import Console

from ai_assistant.commands import HELP_TEXT, SLASH_COMMANDS
from ai_assistant.config import require_config
from ai_assistant.openai_client import Assistant

console = Console()
EXIT_COMMANDS = {"exit", "quit", "çık"}


def _resolve_slash_command(user_input: str) -> Optional[str]:
    """`/` ile başlayan girdiyi ilgili görev şablonuna çevirir. Komut yoksa None döner."""
    body = user_input[1:].strip()
    parts = body.split(maxsplit=1)
    name = parts[0].lower() if parts else ""
    arg = parts[1] if len(parts) > 1 else ""

    if name in ("", "help"):
        console.print(HELP_TEXT)
        return None

    template = SLASH_COMMANDS.get(name)
    if template is None:
        console.print(
            f"[bold red]Bilinmeyen komut:[/bold red] /{name}\n\n{HELP_TEXT}"
        )
        return None

    return template(arg)


def main() -> None:
    require_config()
    assistant = Assistant()

    console.print("[bold cyan]AI Coding Assistant[/bold cyan] — çıkmak için 'exit' yazın.\n")
    console.print("Kısayol komutları için [bold]/help[/bold] yazabilirsiniz.\n")

    while True:
        try:
            user_input = console.input("[bold green]> [/bold green]")
        except (EOFError, KeyboardInterrupt):
            console.print("\nGörüşürüz!")
            break

        if not user_input.strip():
            continue
        if user_input.strip().lower() in EXIT_COMMANDS:
            console.print("Görüşürüz!")
            break

        if user_input.strip().startswith("/"):
            prompt = _resolve_slash_command(user_input.strip())
            if prompt is None:
                continue
        else:
            prompt = user_input

        try:
            reply = assistant.send(prompt)
        except Exception as exc:  # noqa: BLE001 - kullanıcıya hata olarak gösterilir
            console.print(f"[bold red]Hata:[/bold red] {exc}")
            continue

        console.print(f"\n{reply}\n")


if __name__ == "__main__":
    main()
