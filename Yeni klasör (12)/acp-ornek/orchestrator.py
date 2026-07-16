import subprocess
import sys

from transport import send_request, wait_for_port

SEARCH_PORT = 8901
EVALUATOR_PORT = 8902
FINAL_PORT = 8903


def baslat_ajanlar() -> list[subprocess.Popen]:
    procs = [
        subprocess.Popen([sys.executable, "search_agent_server.py"]),
        subprocess.Popen([sys.executable, "evaluator_agent_server.py"]),
        subprocess.Popen([sys.executable, "final_agent_server.py"]),
    ]
    wait_for_port("127.0.0.1", SEARCH_PORT)
    wait_for_port("127.0.0.1", EVALUATOR_PORT)
    wait_for_port("127.0.0.1", FINAL_PORT)
    return procs


def orkestra_et() -> None:
    procs = baslat_ajanlar()
    try:
        print("\n--- planner_agent: 'Ankara'daki en iyi kahveleri bul' görevi veriliyor ---")

        arama_sonucu = send_request(
            "127.0.0.1", SEARCH_PORT, "search_restaurants",
            {"city": "Ankara", "category": "coffee"},
        )

        degerlendirme = send_request(
            "127.0.0.1", EVALUATOR_PORT, "evaluate_restaurants", arama_sonucu,
        )

        nihai = send_request("127.0.0.1", FINAL_PORT, "finalize", degerlendirme)

        print("\n=== Kullanıcıya sunulan sonuç ===")
        for i, k in enumerate(nihai["top_3"], start=1):
            print(
                f"{i}. {k['name']} — puan: {k['rating']} — skor: {k.get('score')} "
                f"— neden: {k.get('reason')}"
            )
    finally:
        for p in procs:
            p.terminate()


if __name__ == "__main__":
    orkestra_et()
