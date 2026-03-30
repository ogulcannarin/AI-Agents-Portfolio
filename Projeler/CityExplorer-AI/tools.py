import requests
import folium
from typing import List, Dict


def search_places(city: str, category: str) -> List[Dict]:
    """
    OpenStreetMap üzerinden belirli bir şehirde ve kategoride mekan arar.
    """

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": f"{category} in {city}",
        "format": "json",
        "limit": 5,
        "addressdetails": 1
    }

    headers = {
        "User-Agent": "CityExplorerAgent/1.0"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)

        if response.status_code != 200:
            print("API hatası:", response.status_code)
            return []

        raw_data = response.json()
        places = []

        for item in raw_data:
            display_name = item.get("display_name", "Bilinmeyen yer")

            places.append({
                "name": display_name.split(",")[0] if display_name else "Bilinmeyen",
                "lat": float(item.get("lat", 0)),
                "lon": float(item.get("lon", 0)),
                "category": category.capitalize(),
                "address": display_name
            })

        return places

    except Exception as e:
        print("Hata oluştu:", e)
        return []


def generate_map(places: List[Dict], filename="map.html"):
    if not places:
        return "Görüntülenecek mekan bulunamadı."

    start_coords = [places[0]['lat'], places[0]['lon']]

    m = folium.Map(
        location=start_coords,
        zoom_start=13,
        tiles="cartodbpositron"
    )

    for place in places:
        category = place['category'].lower()

        # kategoriye göre renk
        if "museum" in category:
            color = "red"
        elif "restaurant" in category:
            color = "blue"
        elif "cafe" in category:
            color = "green"
        else:
            color = "purple"

        folium.Marker(
            location=[place['lat'], place['lon']],
            popup=f"<b>{place['name']}</b><br>{place['category']}",
            tooltip=place['name'],
            icon=folium.Icon(color=color, icon="info-sign")
        ).add_to(m)

    m.save(filename)
    return f"Harita başarıyla oluşturuldu: {filename}"