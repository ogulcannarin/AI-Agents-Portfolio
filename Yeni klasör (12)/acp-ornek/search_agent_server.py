import json
import os
import urllib.error
import urllib.parse
import urllib.request

from transport import serve

API_KEY = os.environ.get("FOURSQUARE_API_KEY")
SEARCH_URL = "https://places-api.foursquare.com/places/search"


def foursquare_ara(city: str, category: str, limit: int = 10) -> list:
    if not API_KEY:
        raise RuntimeError("FOURSQUARE_API_KEY ortam değişkeni tanımlı değil")

    params = {
        "query": category,
        "near": city,
        "limit": limit,
        "fields": "name,location",
    }
    url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "application/json",
            "X-Places-Api-Version": "2025-06-17",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        gövde = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Foursquare API hatası {exc.code}: {gövde}") from exc

    sonuclar = []
    for yer in data.get("results", []):
        sonuclar.append(
            {
                "name": yer.get("name"),
                "rating": yer.get("rating"),
                "review_count": (yer.get("stats") or {}).get("total_ratings"),
            }
        )
    return sonuclar


def handle(method: str, params: dict) -> dict:
    if method != "search_restaurants":
        raise ValueError(f"bilinmeyen method: {method}")
    print(f"[search_agent] Foursquare'den '{params['city']}' - '{params['category']}' aranıyor...")
    sonuclar = foursquare_ara(params["city"], params["category"])
    return {"results": sonuclar}


if __name__ == "__main__":
    serve(8901, handle)
