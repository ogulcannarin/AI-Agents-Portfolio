"""Git yardımcı araçları: salt okunur diff görüntüleme ve onaylı commit.

Bu modül, git ile etkileşim kurmayı sağlayan fonksiyonlar içerir. Kullanıcı, git deposu olup olmadığını kontrol edebilir,
değişiklikleri görebilir ve commit işlemi gerçekleştirebilir.
"""
import subprocess

from ai_assistant import diff_utils

NOT_A_REPO_MSG = "Hata: Bu dizin bir git deposu değil. Önce 'git init' çalıştırılmalı."


def _is_git_repo() -> bool:
    """Mevcut dizinin bir git deposu olup olmadığını kontrol eder."""
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def git_diff() -> str:
    """Mevcut değişiklikleri gösterir. Staged ve unstaged değişiklikleri ayırt eder.

    Returns:
        str: Değişikliklerin durumu ve içeriği.
    """
    if not _is_git_repo():
        return NOT_A_REPO_MSG

    status = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    if not status.stdout.strip():
        return "Değişiklik yok, çalışma dizini temiz."

    parts = [f"git status --short:\n{status.stdout}"]

    diff = subprocess.run(["git", "diff"], capture_output=True, text=True)
    if diff.stdout.strip():
        parts.append(f"Staged olmayan değişiklikler (git diff):\n{diff.stdout}")

    staged_diff = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    if staged_diff.stdout.strip():
        parts.append(f"Staged değişiklikler (git diff --staged):\n{staged_diff.stdout}")

    return "\n\n".join(parts)


def git_commit(message: str) -> str:
    """Belirtilen mesajla tüm değişiklikleri commit eder.

    Args:
        message (str): Commit için kullanılacak mesaj.

    Returns:
        str: Commit işleminin sonucu.
    """
    if not _is_git_repo():
        return NOT_A_REPO_MSG

    print(f'\nÖnerilen commit mesajı:\n\n  "{message}"\n')
    if not diff_utils.confirm("Bu mesajla tüm değişiklikleri commit'lemek istiyor musunuz?"):
        return "Kullanıcı commit işlemini reddetti."

    add_result = subprocess.run(["git", "add", "-A"], capture_output=True, text=True)
    if add_result.returncode != 0:
        return f"Hata: git add başarısız oldu:\n{add_result.stderr}"

    commit_result = subprocess.run(
        ["git", "commit", "-m", message], capture_output=True, text=True
    )
    if commit_result.returncode != 0:
        return f"Hata: git commit başarısız oldu:\n{commit_result.stderr}"

    return f"Commit oluşturuldu:\n{commit_result.stdout}"