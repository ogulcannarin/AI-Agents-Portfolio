from state import ExplorerState
from tools import search_places
from map_tool import generate_map
import json

def museum_agent(state: ExplorerState):
    """Müzeleri bulmaktan sorumlu ajan."""
    print(f"--- {state['location']} bölgesinde müzeler aranıyor... ---")
    
    # Tools dosyasındaki arama fonksiyonunu kullanıyoruz
    museums = search_places(state['location'], "museum")
    
    # Mevcut bulunan mekanlara ekleme yapıyoruz
    current_places = state.get("found_places", [])
    current_places.extend(museums)
    
    return {"found_places": current_places}

def food_agent(state: ExplorerState):
    """Yemek yerlerini bulmaktan sorumlu ajan."""
    print(f"--- {state['location']} bölgesinde restoranlar aranıyor... ---")
    
    restaurants = search_places(state['location'], "restaurant")
    
    current_places = state.get("found_places", [])
    current_places.extend(restaurants)
    
    return {"found_places": current_places}

def map_node(state: ExplorerState):
    """Toplanan tüm verilerden harita ve JSON oluşturan düğüm."""
    print("--- Harita ve JSON verisi hazırlanıyor... ---")
    
    places = state["found_places"]
    
    # Haritayı oluştur (HTML dosyası olarak kaydeder)
    map_result = generate_map(places)
    
    # JSON çıktısını hazırla
    final_json = json.dumps(places, indent=4, ensure_ascii=False)
    
    return {"final_json": final_json, "map_url": map_result}