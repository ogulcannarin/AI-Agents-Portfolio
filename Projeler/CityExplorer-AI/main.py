from graph import app
import json

def start_explorer(city_name: str):
    print(f"\n{'='*10} {city_name.upper()} KEŞFİ BAŞLIYOR {'='*10}")
    
    # Başlangıç durumu
    initial_state = {
        "location": city_name,
        "interests": ["museum", "restaurant"],
        "found_places": []
    }
    
    # Grafı çalıştır
    final_output = app.invoke(initial_state)
    
    # JSON Çıktısını Ekrana Bas
    print("\n--- OLUŞTURULAN JSON VERİSİ ---")
    print(final_output["final_json"])
    
    # Harita Durumu
    print(f"\n--- SONUÇ ---")
    print(final_output["map_url"])
    print(f"{'='*40}\n")

if __name__ == "__main__":
    # Test için bir şehir yazalım
    start_explorer("Beşiktaş")