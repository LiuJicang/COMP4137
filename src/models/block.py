"""Block model and mining behavior."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from src.crypto.hash_utils import hash_json
from src.mining.pow import meets_difficulty


@dataclass
class Block:
    index: int
    previous_hash: str
    merkle_root: str
    transactions: list[dict]
    difficulty: int
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    nonce: int = 0
    block_hash: str = ""

    def header_payload(self) -> dict:
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "merkle_root": self.merkle_root,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "difficulty": self.difficulty,
        }

    def calculate_hash(self) -> str:
        return hash_json(self.header_payload())

    def mine(self) -> None:
        while True:
            candidate = self.calculate_hash()
            if meets_difficulty(candidate, self.difficulty):
                self.block_hash = candidate
                return
            self.nonce += 1
