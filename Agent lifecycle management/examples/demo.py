"""Temel kullanım: bir ajanı başlat, tamamlanana kadar çalıştır."""

import time

from agent_lifecycle import AgentManager, AgentRun, AgentStore


def fake_llm_step(run: AgentRun) -> dict:
    """Gerçek LLM çağrısının yerine geçen örnek fonksiyon."""
    print(f"[{run.id}] adım {run.step}: '{run.task}' üzerinde çalışıyor...")
    time.sleep(0.2)
    return {"done": run.step >= 2}


if __name__ == "__main__":
    store = AgentStore()
    manager = AgentManager(store, fake_llm_step)

    run = manager.start("Rakip analizi raporu hazırla", max_steps=10, deadline_s=30)
    print(f"\nSonuç: {run.id} -> {run.state.value}, toplam adım: {run.step}")
    print(f"Kayıtlı çalıştırmalar: {store.list_runs()}")
