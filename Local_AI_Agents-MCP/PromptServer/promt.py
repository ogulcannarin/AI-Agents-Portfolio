from mcp.server.fastmcp import FastMCP
import os
import platform

# Sunucumuza bir isim verelim
mcp = FastMCP("MyLocalAgent")

# --- RESOURCE: Sistem Bilgisi ---
@mcp.resource("system://info")
def get_system_info() -> str:
    """İşletim sistemi bilgisini döner"""
    return f"İşletim Sistemi: {platform.system()}, Versiyon: {platform.release()}"

# --- TOOL: Klasör İçeriğini Listele ---
@mcp.tool()
def list_files(path: str = ".") -> list:
    """Belirtilen dizindeki dosyaları listeler"""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Hata: {str(e)}"]

# --- TOOL: Dosya Oku ---
@mcp.tool()
def read_file(path: str) -> str:
    """Belirtilen dosyanın içeriğini okur"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Hata: {str(e)}"

# --- PROMPT: Kod İnceleme Şablonu ---
@mcp.prompt("analyze-code")
def analyze_code_prompt(code: str) -> str:
    return f"""
Aşağıdaki kodu bir uzman yazılım mimarı gözüyle incele:

KOD:
{code}

Lütfen şu kriterlere göre analiz yap:
1. Güvenlik açıkları (Security)
2. Performans iyileştirmeleri
3. Pythonic yazım kuralları (PEP8)
"""

if __name__ == "__main__":
    mcp.run()