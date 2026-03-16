from mcp.server.fastmcp import FastMCP
import logging

# 1. Akademik Logging Yapılandırması
# Bu loglar hem senin terminalinde görünür hem de MCP üzerinden Host'a iletilebilir.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RobustAuditor")

mcp = FastMCP("RobustAuditor")

@mcp.tool()
def safe_file_analyzer(file_path: str) -> str:
    """Hata yönetimi yapılmış, güvenli dosya analiz aracı."""
    
    logger.info(f"Analiz isteği alındı: {file_path}")
    
    # KONTROL 1: Dosya yolu boş mu?
    if not file_path:
        logger.warning("Boş dosya yolu gönderildi!")
        return "HATA: Dosya yolu boş olamaz."

    try:
        # KONTROL 2: Dosyayı açmaya çalış (İzin veya dosya yoksa hata fırlatır)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        logger.info(f"Dosya başarıyla okundu. Karakter sayısı: {len(content)}")
        return f"Analiz Başarılı! Dosya Boyutu: {len(content)} karakter."

    except FileNotFoundError:
        logger.error(f"Dosya bulunamadı: {file_path}")
        return f"HATA: '{file_path}' dosyası sistemde bulunamadı. Lütfen yolu kontrol et."
    
    except PermissionError:
        logger.error(f"Erişim engellendi: {file_path}")
        return "HATA: Bu dosyayı okumak için yetkim yok."
    
    except Exception as e:
        logger.critical(f"Beklenmeyen hata: {str(e)}")
        return f"Sistemsel bir hata oluştu: {str(e)}"

if __name__ == "__main__":
    mcp.run()