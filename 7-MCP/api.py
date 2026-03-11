import httpx # İnternetten veri çekmek için (pip install httpx)
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Akıllı Asistan")

@mcp.tool()
async def hava_durumu_getir(sehir: str) -> str:
    """Belirtilen şehrin güncel hava durumunu internetten çeker."""
    # Örnek bir ücretsiz API kullanıyoruz (Open-Meteo gibi)
    # Not: Gerçek projelerde buraya kendi API anahtarını eklersin.
    url = f"https://wttr.in/{sehir}?format=3" 
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        return "Hava durumu bilgisi alınamadı."

if __name__ == "__main__":
    mcp.run()