import json
import random


def yazdir_mesaj(mesaj: dict) -> None:
    print(f"\n>>> ACP mesajı: {mesaj['from']} -> {mesaj['to']} ({mesaj['type']})")
    print(json.dumps(mesaj, ensure_ascii=False, indent=2))


def acp_mesaj(gonderen: str, alan: str, tur: str, **alanlar) -> dict:
    return {"from": gonderen, "to": alan, "type": tur, **alanlar}


# --- 1. Planner Agent ---
def planner_agent(hedef: str) -> dict:
    # Kullanıcının doğal dil hedefini somut bir görev mesajına çevirir.
    return acp_mesaj(
        "planner_agent",
        "search_agent",
        "task",
        task="search_restaurants",
        input={"city": "Ankara", "category": "coffee"},
    )


# --- 2 & 3. Search Agent ---
MOCK_KAHVECILER = [
    {"name": "Kahveci A", "rating": 4.6, "review_count": 210},
    {"name": "Kahveci B", "rating": 4.2, "review_count": 85},
    {"name": "Kahveci C", "rating": 4.8, "review_count": 40},
    {"name": "Kahveci D", "rating": 3.9, "review_count": 300},
]


def search_agent(gorev_mesaji: dict) -> dict:
    sehir = gorev_mesaji["input"]["city"]
    kategori = gorev_mesaji["input"]["category"]
    print(f"[search_agent] '{sehir}' şehrinde '{kategori}' aranıyor...")

    return acp_mesaj(
        "search_agent",
        "evaluator_agent",
        "result",
        task="search_restaurants",
        output={"results": MOCK_KAHVECILER},
    )


# --- 4. Evaluator Agent ---
def evaluator_agent(sonuc_mesaji: dict) -> dict:
    kahveciler = sonuc_mesaji["output"]["results"]

    def skor(k: dict) -> float:
        # basit bir skorlama: puan ağırlıklı, yorum sayısı ikincil etken
        return k["rating"] * 0.8 + min(k["review_count"], 200) / 200 * 0.2 * 5

    skorlanmis = [{**k, "score": round(skor(k), 2)} for k in kahveciler]
    skorlanmis.sort(key=lambda k: k["score"], reverse=True)

    return acp_mesaj(
        "evaluator_agent",
        "final_agent",
        "result",
        task="evaluate_restaurants",
        output={"ranked": skorlanmis},
    )


# --- 5. Final Agent ---
def final_agent(degerlendirme_mesaji: dict) -> dict:
    en_iyi_3 = degerlendirme_mesaji["output"]["ranked"][:3]

    return acp_mesaj(
        "final_agent",
        "user",
        "final_answer",
        output={"top_3": en_iyi_3},
    )


def orkestra_et(kullanici_hedefi: str) -> None:
    gorev = planner_agent(kullanici_hedefi)
    yazdir_mesaj(gorev)

    arama_sonucu = search_agent(gorev)
    yazdir_mesaj(arama_sonucu)

    degerlendirme = evaluator_agent(arama_sonucu)
    yazdir_mesaj(degerlendirme)

    nihai_cevap = final_agent(degerlendirme)
    yazdir_mesaj(nihai_cevap)

    print("\n=== Kullanıcıya sunulan sonuç ===")
    for i, k in enumerate(nihai_cevap["output"]["top_3"], start=1):
        print(f"{i}. {k['name']} — puan: {k['rating']} — skor: {k['score']}")


if __name__ == "__main__":
    orkestra_et("Ankara'daki en iyi kahveleri bul")
