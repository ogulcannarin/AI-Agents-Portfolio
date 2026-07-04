"""Dosya sistemi araçları: listeleme, okuma, onaylı yazma."""
import os

from ai_assistant import diff_utils

IGNORED_DIRS = {".git", "venv", ".venv", "__pycache__", "node_modules", ".idea", ".vscode"}


def list_files(path: str = ".", max_entries: int = 500) -> str:
    root = os.path.abspath(path)
    if not os.path.isdir(root):
        return f"Hata: '{path}' bir dizin değil veya bulunamadı."

    lines = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        rel_dir = os.path.relpath(dirpath, root)
        for filename in filenames:
            rel_path = filename if rel_dir == "." else os.path.join(rel_dir, filename)
            lines.append(rel_path)
            if len(lines) >= max_entries:
                lines.append(f"... (ilk {max_entries} dosya gösterildi)")
                return "\n".join(lines)
    if not lines:
        return "(dizin boş)"
    return "\n".join(lines)


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        return f"Hata: '{path}' bulunamadı."
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        return f"Hata: '{path}' metin olarak okunamadı (muhtemelen ikili/binary dosya)."

    numbered = "\n".join(f"{i + 1}\t{line}" for i, line in enumerate(content.splitlines()))
    return numbered if numbered else "(dosya boş)"


def write_file(path: str, content: str) -> str:
    exists = os.path.isfile(path)
    old_content = ""
    if exists:
        try:
            with open(path, "r", encoding="utf-8") as f:
                old_content = f.read()
        except UnicodeDecodeError:
            return f"Hata: '{path}' metin olarak okunamadı, üzerine yazma reddedildi."

    if old_content == content:
        return f"'{path}' zaten önerilen içerikle aynı, değişiklik yapılmadı."

    label = "Değiştirilecek dosya" if exists else "Oluşturulacak yeni dosya"
    print(f"\n{label}: {path}")
    diff_utils.print_diff(diff_utils.build_diff(path, old_content, content))

    if not diff_utils.confirm(f"'{path}' dosyasına bu değişikliği uygulamak istiyor musunuz?"):
        return "Kullanıcı bu değişikliği reddetti, dosya değiştirilmedi."

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"'{path}' başarıyla {'güncellendi' if exists else 'oluşturuldu'}."
