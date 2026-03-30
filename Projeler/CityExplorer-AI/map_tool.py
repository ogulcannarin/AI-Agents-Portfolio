import folium
from typing import List, Dict
def generate_map(places: List[Dict], filename="map.html"):
    """
    JSON formatındaki mekan listesini alır ve interaktif bir harita oluşturur.
    """
    if not places:
        return "Görüntülenecek mekan bulunamadı."

    # Haritayı ilk mekanın koordinatlarına odakla
    start_coords = [places[0]['lat'], places[0]['lon']]
    m = folium.Map(location=start_coords, zoom_start=13)

    # Her mekanı haritaya ekle
    for place in places:
        color = "blue"
        if "Museum" in place['category']: color = "red"
        elif "Restaurant" in place['category']: color = "green"
        
        folium.Marker(
            location=[place['lat'], place['lon']],
            popup=f"<b>{place['name']}</b><br>{place['category']}",
            tooltip=place['name'],
            icon=folium.Icon(color=color, icon="info-sign")
        ).add_to(m)

    m.save(filename)
    return f"Harita başarıyla oluşturuldu: {filename}"