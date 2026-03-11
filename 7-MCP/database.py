import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Veritabanı Asistanı")

# Veritabanını hazırlayalım (Örnek bir Notlar tablosu)
def init_db():
    conn = sqlite3.connect("hafiza.db")
    conn.execute("CREATE TABLE IF NOT EXISTS notlar (id INTEGER PRIMARY KEY, icerik TEXT)")
    conn.commit()
    conn.close()

init_db()

# DERS 7.1: Veri Ekleme Aracı (Tool)
@mcp.tool()
def not_ekle(icerik: str) -> str:
    """Veritabanına yeni bir not kaydeder."""
    conn = sqlite3.connect("hafiza.db")
    conn.execute("INSERT INTO notlar (icerik) VALUES (?)", (icerik,))
    conn.commit()
    conn.close()
    return "Not başarıyla kaydedildi!"

# DERS 7.2: Veri Sorgulama Aracı (Tool)
@mcp.tool()
def notlari_listele() -> list:
    """Veritabanındaki tüm notları getirir."""
    conn = sqlite3.connect("hafiza.db")
    cursor = conn.cursor()
    cursor.execute("SELECT icerik FROM notlar")
    notlar = [row[0] for row in cursor.fetchall()]
    conn.close()
    return notlar

if __name__ == "__main__":
    mcp.run()