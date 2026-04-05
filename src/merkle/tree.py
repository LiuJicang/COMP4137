"""Merkle tree construction from transaction ids."""

from __future__ import annotations

from src.crypto.hash_utils import hash_text


def build_merkle_root(tx_ids: list[str]) -> str:
    if not tx_ids:
        return hash_text("")

    level = [hash_text(tx_id) for tx_id in tx_ids]
    while len(level) > 1:
        next_level: list[str] = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else level[i]
            next_level.append(hash_text(left + right))
        level = next_level

    return level[0]
