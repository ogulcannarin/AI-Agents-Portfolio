from mcp.server.fastmcp import FastMCP
import httpx
import sqlite3

mcp = FastMCP("Super_Asistan")

# --- VERİTABANI KATMANI ---
@mcp.tool()
def plan_guncelle(eski_plan: str, yeni_plan: str) -> str:
    """Veritabanındaki spesifik bir planı yenisiyle değiştirir."""
    conn = sqlite3.connect("hafiza.db") # Senin hafiza.db dosyanı kullanıyoruz
    cursor = conn.cursor()
    cursor.execute("UPDATE notlar SET icerik = ? WHERE icerik LIKE ?", 
                  (yeni_plan, f"%{eski_plan}%"))
    conn.commit()
    conn.close()
    return f"'{eski_plan}' içeren planlar '{yeni_plan}' olarak güncellendi."

# --- API KATMANI ---
@mcp.tool()
async def hava_durumu_sayisal(sehir: str) -> dict:
    """Hava durumunu sadece metin değil, sayısal veri (JSON) olarak döner."""
    # Ajanın kıyaslama yapabilmesi için sayısal veri dönmek daha sağlıklıdır
    async with httpx.AsyncClient() as client:
        # Örnek: Elazığ için veri çekiyoruz
        resp = await client.get(f"https://wttr.in/{sehir}?format=j1")
        data = resp.json()
        temp = data['current_condition'][0]['temp_C']
        return {"sehir": sehir, "sicaklik": int(temp)}

# --- ANALİZ KATMANI (Kritik Ders) ---
@mcp.tool()
def aksiyon_karari_ver(sicaklik: int, plan_listesi: list) -> str:
    """Sıcaklık ve planlara bakarak ne yapılması gerektiğini söyler."""
    if sicaklik < 10 and any("yürüyüş" in p.lower() for p in plan_listesi):
        return "Guncelleme_Gerekli"
    return "Her_Sey_Yolunda"

if __name__ == "__main__":
    mcp.run()
