from typing import List, TypedDict, Dict

class Place(TypedDict):
    """Her bir mekanın sahip olması gereken bilgiler."""
    name: str          # Mekan adı
    lat: float         # Enlem (Latitude)
    lon: float         # Boylam (Longitude)
    category: str      # 'Müze', 'Restoran', 'Kafe' vb.
    address: str       # Açık adres

class ExplorerState(TypedDict):
    """Ajanlar arası paylaşılan genel durum."""
    location: str               # Kullanıcının gitmek istediği yer (örn: Kadıköy)
    interests: List[str]        # İlgi alanları (örn: ['müze', 'restoran'])
    found_places: List[Dict]    # Uzman ajanların bulduğu tüm mekanların listesi
    final_json: str             # Tüm verilerin birleşmiş JSON hali
    map_url: str                # Oluşturulan .html haritasının yolu