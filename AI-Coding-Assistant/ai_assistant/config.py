"""Ortam değişkenlerinden (.env dahil) yapılandırmayı okur."""
import os
import sys

from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "gpt-4o-mini"


class ConfigError(Exception):
    pass


def get_api_key() -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ConfigError(
            "OPENAI_API_KEY bulunamadı. Proje kök dizininde bir .env dosyası "
            "oluşturup OPENAI_API_KEY=... satırını ekleyin (bkz. .env.example)."
        )
    return api_key


def get_model() -> str:
    return os.environ.get("AI_ASSISTANT_MODEL", DEFAULT_MODEL)


def require_config() -> None:
    """API key eksikse kullanıcıya net bir mesajla programı sonlandırır."""
    try:
        get_api_key()
    except ConfigError as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        sys.exit(1)
