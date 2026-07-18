"""Ajan durumunu diske kaydeden/okuyan persistence katmanı."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .run import AgentRun
from .states import AgentState


class AgentStore:
    def __init__(self, dir_path: str = "./agent_runs"):
        self.dir = Path(dir_path)
        self.dir.mkdir(exist_ok=True)

    def _path(self, run_id: str) -> Path:
        return self.dir / f"{run_id}.json"

    def save(self, run: AgentRun) -> None:
        data = asdict(run)
        self._path(run.id).write_text(json.dumps(data, default=str, indent=2))

    def load(self, run_id: str) -> AgentRun:
        raw = json.loads(self._path(run_id).read_text())
        raw["state"] = AgentState(raw["state"])
        return AgentRun(**raw)

    def list_runs(self) -> list[str]:
        return [p.stem for p in self.dir.glob("*.json")]
