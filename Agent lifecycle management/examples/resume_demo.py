"""Yaşam döngüsünün asıl kazandırdığı şey: kaldığı yerden devam edebilme.

Senaryo:
  1. Ajan 2 adım çalışır, sonra insan onayı beklemek için WAITING durumuna geçer.
  2. Süreç burada "çökmüş" gibi davranır (yeni bir AgentManager/AgentStore ile devam ederiz).
  3. Diskten run_id ile yükleyip resume() çağırarak kaldığı adımdan devam ettiririz.
"""

import time

from agent_lifecycle import AgentManager, AgentRun, AgentStore


def approval_gated_step(run: AgentRun) -> dict:
    if run.step == 2:
        return {"needs_input": True}
    return {"done": run.step >= 4}


if __name__ == "__main__":
    store = AgentStore()
    manager = AgentManager(store, approval_gated_step)

    run = manager.start("Fatura onayı iste", max_steps=10, deadline_s=30)
    print(f"İlk çalışma durdu: {run.id} -> {run.state.value} (adım {run.step})")

    # --- burada süreç yeniden başlamış gibi davranıyoruz ---
    time.sleep(0.5)
    fresh_store = AgentStore()
    fresh_manager = AgentManager(fresh_store, approval_gated_step)

    resumed = fresh_manager.resume(run.id)
    print(f"Devam ettirildi: {resumed.id} -> {resumed.state.value} (adım {resumed.step})")
    print("Geçiş geçmişi:")
    for h in resumed.history:
        print(f"  {h['from']} -> {h['to']} (adım {h['step']})")
