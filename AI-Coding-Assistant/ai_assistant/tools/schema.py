"""OpenAI tool-calling için JSON schema tanımları ve dispatch tablosu."""
from ai_assistant.tools.files import list_files, read_file, write_file
from ai_assistant.tools.git import git_commit, git_diff
from ai_assistant.tools.shell import run_command

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "Verilen dizindeki dosyaları (alt dizinler dahil) listeler.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Listelenecek dizin yolu. Varsayılan: mevcut dizin.",
                    }
                },
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Bir dosyanın içeriğini satır numaralarıyla birlikte okur.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Okunacak dosyanın yolu."}
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": (
                "Bir dosyaya yeni içerik yazar (dosya yoksa oluşturur). "
                "Uygulanmadan önce kullanıcıya diff gösterilip onay istenir."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Yazılacak dosyanın yolu."},
                    "content": {
                        "type": "string",
                        "description": "Dosyanın yeni tam içeriği (eski içeriğin yerine geçer).",
                    },
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": (
                "Bir shell komutu çalıştırır. Çalıştırılmadan önce kullanıcıya "
                "onay sorulur."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "Çalıştırılacak shell komutu."}
                },
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "git_diff",
            "description": (
                "Çalışma dizinindeki git değişikliklerini gösterir (git status + "
                "staged/unstaged diff). Salt okunur, onay gerekmez."
            ),
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "git_commit",
            "description": (
                "Verilen commit mesajını kullanıcıya gösterip onay ister; onaylanırsa "
                "tüm değişiklikleri stage edip ('git add -A') commit atar."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Önerilen commit mesajı (Conventional Commits formatında tercih edilir).",
                    }
                },
                "required": ["message"],
            },
        },
    },
]

DISPATCH = {
    "list_files": lambda args: list_files(args.get("path", ".")),
    "read_file": lambda args: read_file(args["path"]),
    "write_file": lambda args: write_file(args["path"], args["content"]),
    "run_command": lambda args: run_command(args["command"]),
    "git_diff": lambda args: git_diff(),
    "git_commit": lambda args: git_commit(args["message"]),
}
