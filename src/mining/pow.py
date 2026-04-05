"""Proof-of-work helpers."""

from __future__ import annotations


def meets_difficulty(hash_value: str, difficulty: int) -> bool:
    return hash_value.startswith("0" * difficulty)
