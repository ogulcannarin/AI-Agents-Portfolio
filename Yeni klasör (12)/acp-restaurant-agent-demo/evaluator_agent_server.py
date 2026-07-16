import json
import os

from openai import OpenAI

from transport import serve

client = OpenAI()
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")


def handle(method: str, params: dict) -> dict:
    if method != "evaluate_restaurants":
        raise ValueError(f"bilinmeyen method: {method}")

    restaurants = params["results"]
    prompt = (
        "Aşağıdaki kahvecileri değerlendir. rating ve review_count doluysa "
        "bunları dikkate alarak en iyiden en kötüye sırala. Bu alanlar null "
        "ise (veri sağlayıcıda mevcut değilse) listeyi eleme, tüm mekanları "
        "yine de 'ranked' listesine dahil et; bu durumda score alanını null "
        "bırak ve reason alanına 'puan verisi mevcut değil' gibi bir not yaz. "
        "Hiçbir mekanı listeden çıkarma. Sadece geçerli JSON döndür, başka "
        "hiçbir metin ekleme. Format:\n"
        '{"ranked": [{"name": str, "rating": float | null, '
        '"review_count": int | null, "score": float | null, "reason": str}, ...]}\n\n'
        f"Kahveciler: {json.dumps(restaurants, ensure_ascii=False)}"
    )

    print("[evaluator_agent] OpenAI'dan değerlendirme isteniyor...")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    serve(8902, handle)
