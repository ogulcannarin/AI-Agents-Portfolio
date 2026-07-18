"""Bir ajan çalıştırmasının tüm yaşam döngüsünü yöneten orkestratör."""

from __future__ import annotations

from typing import Callable

from .run import AgentRun
from .states import AgentState
from .store import AgentStore


class AgentManager:
    def __init__(self, store: AgentStore, llm_step: Callable[[AgentRun], dict]):
        self.store = store
        self.llm_step = llm_step  # her adımda çağrılan fonksiyon (gerçek LLM çağrın)

    def start(self, task: str, **kwargs) -> AgentRun:
        run = AgentRun(task=task, **kwargs)
        run.transition(AgentState.RUNNING)
        self.store.save(run)
        return self._loop(run)

    def resume(self, run_id: str) -> AgentRun:
        run = self.store.load(run_id)
        if run.is_finished():
            return run  # zaten bitmiş, tekrar çalıştırmaya gerek yok
        run.transition(AgentState.RUNNING)
        self.store.save(run)
        return self._loop(run)

    def pause(self, run_id: str) -> AgentRun:
        run = self.store.load(run_id)
        run.transition(AgentState.PAUSED)
        self.store.save(run)
        return run

    def _loop(self, run: AgentRun) -> AgentRun:
        while run.state == AgentState.RUNNING:
            if run.is_expired():
                run.transition(AgentState.TIMED_OUT)
                break
            if run.step >= run.max_steps:
                run.transition(AgentState.TIMED_OUT)
                break

            try:
                result = self.llm_step(run)  # tek bir LLM adımı / tool çağrısı
            except Exception as e:
                run.error = str(e)
                run.transition(AgentState.FAILED)
                self.store.save(run)
                raise

            run.step += 1

            if result.get("done"):
                run.transition(AgentState.COMPLETED)
            elif result.get("needs_input"):
                run.transition(AgentState.WAITING)
            # aksi halde RUNNING durumunda devam eder

            self.store.save(run)

        return run
