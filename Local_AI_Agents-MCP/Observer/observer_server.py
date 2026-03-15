from mcp.server.fastmcp import FastMCP
import logging
import datetime

# 1. Akademik Logging: Sunucunun yaşam döngüsünü terminalden izleyelim
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ProjectObserver")

mcp = FastMCP("ProjectObserver")

# --- INITIALIZATION LOGIC ---
# Bu değişken sunucu "yaşadığı" sürece bellekte kalacak (State Management)
start_time = datetime.datetime.now()

@mcp.resource("observer://uptime")
def get_uptime() -> str:
    """Sunucunun ne kadar süredir hayatta olduğunu (lifecycle) döner."""
    delta = datetime.datetime.now() - start_time
    return f"Sunucu {delta} süredir aktif ve sağlıklı çalışıyor."

@mcp.tool()
def check_project_health(path: str = ".") -> str:
    """Proje klasöründeki dosyaları analiz eder ve bir 'sağlık raporu' sunar."""
    import os
    try:
        files = os.listdir(path)
        py_files = [f for f in files if f.endswith('.py')]
        logger.info(f"Analiz başlatıldı: {len(py_files)} Python dosyası bulundu.") # Runtime notification
        
        return f"Analiz Tamamlandı: {len(files)} toplam dosya, {len(py_files)} Python dosyası mevcut."
    except Exception as e:
        logger.error(f"Hata oluştu: {str(e)}")
        return f"Hata: {str(e)}"

if __name__ == "__main__":
    # Sunucu burada 'Initialize' aşamasına giriyor
    logger.info("Observer sunucusu el sıkışma (handshake) için hazır.")
    mcp.run()