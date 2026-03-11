from mcp.server.fastmcp import FastMCP
import httpx
import sqlite3

mcp = FastMCP("Stratejik Planlayıcı")

# 1. ARAÇ: Hava Durumu (Dış Dünya Verisi)
@mcp.tool()
async def hava_durumu_analizi(sehir: str) -> dict:
    """Hava durumunu detaylı (sıcaklık ve yağış) olarak döner."""
    # Simüle edilmiş veri (veya wttr.in/sehir?format=j1 gibi bir API)
    return {"sicaklik": 12, "yagis_var_mi": True}

# 2. ARAÇ: Takvim/Notlar (Kişisel Veri)
@mcp.tool()
def planlari_kontrol_et() -> str:
    """Kullanıcının bugünkü etkinliklerini döner."""
    return "Saat 15:00'da parkta yürüyüş planı var."

# 3. ARAÇ: Tavsiye Motoru (Mantıksal Çıktı)
@mcp.tool()
def tavsiye_olustur(durum: str) -> str:
    """Verilen duruma göre nihai tavsiyeyi hazırlar."""
    return f"Analiz sonucuna göre tavsiyem: {durum}"

if __name__ == "__main__":
    mcp.run()