"""Onaylı komut çalıştırma aracı."""
import subprocess

from ai_assistant import diff_utils

DEFAULT_TIMEOUT = 60


def run_command(command: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    print(f"\nÇalıştırılacak komut: {command}")
    if not diff_utils.confirm("Bu komutu çalıştırmak istiyor musunuz?"):
        return "Kullanıcı bu komutu reddetti, çalıştırılmadı."

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return f"Hata: Komut {timeout} saniye içinde tamamlanmadı ve durduruldu."

    parts = [f"exit_code: {result.returncode}"]
    if result.stdout:
        parts.append(f"stdout:\n{result.stdout}")
    if result.stderr:
        parts.append(f"stderr:\n{result.stderr}")
    return "\n".join(parts)
