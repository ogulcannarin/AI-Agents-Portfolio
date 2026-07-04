"""Unified diff üretimi ve terminalde renkli gösterim."""
import difflib

from rich.console import Console

console = Console()


def build_diff(path: str, old_content: str, new_content: str) -> str:
    old_lines = old_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)
    diff = difflib.unified_diff(
        old_lines, new_lines, fromfile=f"a/{path}", tofile=f"b/{path}"
    )
    return "".join(diff)


def print_diff(diff_text: str) -> None:
    if not diff_text:
        console.print("[dim](değişiklik yok)[/dim]")
        return
    for line in diff_text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            console.print(line, style="green")
        elif line.startswith("-") and not line.startswith("---"):
            console.print(line, style="red")
        elif line.startswith("@@"):
            console.print(line, style="cyan")
        else:
            console.print(line, style="dim")


def confirm(prompt: str) -> bool:
    answer = console.input(f"[bold yellow]{prompt}[/bold yellow] [y/N]: ")
    return answer.strip().lower() in ("y", "yes", "e", "evet")
