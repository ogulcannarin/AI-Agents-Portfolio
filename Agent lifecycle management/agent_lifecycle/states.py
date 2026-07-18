"""Ajanın geçebileceği durumlar ve aralarındaki izinli geçişler."""

from __future__ import annotations

from enum import Enum


class AgentState(str, Enum):
    CREATED = "created"        # ajan tanımlandı, henüz başlamadı
    RUNNING = "running"        # aktif olarak adım atıyor (LLM çağrısı / tool kullanımı)
    WAITING = "waiting"        # bir tool sonucunu / insan onayını bekliyor
    PAUSED = "paused"          # kullanıcı ya da sistem tarafından duraklatıldı
    COMPLETED = "completed"    # görev başarıyla bitti
    FAILED = "failed"          # hata ile sonlandı
    TIMED_OUT = "timed_out"    # süre/adım limiti aşıldı


# Geçersiz bir geçişi (örn. COMPLETED -> RUNNING) engellemek için durum makinesi
ALLOWED_TRANSITIONS: dict[AgentState, set[AgentState]] = {
    AgentState.CREATED: {AgentState.RUNNING},
    AgentState.RUNNING: {
        AgentState.WAITING,
        AgentState.PAUSED,
        AgentState.COMPLETED,
        AgentState.FAILED,
        AgentState.TIMED_OUT,
    },
    AgentState.WAITING: {AgentState.RUNNING, AgentState.FAILED, AgentState.TIMED_OUT},
    AgentState.PAUSED: {AgentState.RUNNING},
    AgentState.COMPLETED: set(),
    AgentState.FAILED: set(),
    AgentState.TIMED_OUT: set(),
}
