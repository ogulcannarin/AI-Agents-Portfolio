"""Tek bir ajan çalıştırmasını (AgentRun) temsil eden veri modeli."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional

from .states import ALLOWED_TRANSITIONS, AgentState


@dataclass
class AgentRun:
    task: str
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    state: AgentState = AgentState.CREATED
    step: int = 0
    max_steps: int = 20
    started_at: float = field(default_factory=time.time)
    deadline_s: float = 120.0          # bu saniyeyi geçerse TIMED_OUT
    history: list[dict[str, Any]] = field(default_factory=list)
    error: Optional[str] = None

    def transition(self, new_state: AgentState) -> None:
        if new_state not in ALLOWED_TRANSITIONS[self.state]:
            raise ValueError(f"Geçersiz geçiş: {self.state} -> {new_state}")
        self.history.append({
            "from": self.state, "to": new_state, "at": time.time(), "step": self.step
        })
        self.state = new_state

    def is_finished(self) -> bool:
        return self.state in {AgentState.COMPLETED, AgentState.FAILED, AgentState.TIMED_OUT}

    def is_expired(self) -> bool:
        return (time.time() - self.started_at) > self.deadline_s
