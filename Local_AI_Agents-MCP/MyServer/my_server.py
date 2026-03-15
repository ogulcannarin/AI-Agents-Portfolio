from mcp.server.fastmcp import FastMCP
import os
import platform

# Sunucumuza bir isim verelim
mcp = FastMCP("MyLocalAgent")

# --- RESOURCE: Sistem Bilgisi ---
# Model bu kaynağı okuyarak hangi işletim sisteminde olduğunu anlar.
@mcp.resource("system://info")
def get_system_info() -> str:
    return f"İşletim Sistemi: {platform.system()}, Versiyon: {platform.release()}"

# --- TOOL: Klasör İçeriğini Listele ---
# Model bu aracı kullanarak senin bilgisayarındaki dosyaları görebilir.
@mcp.tool()
def list_files(path: str = ".") -> list:
    """Belirtilen dizindeki dosyaları listeler."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Hata: {str(e)}"]

if __name__ == "__main__":
    mcp.run()