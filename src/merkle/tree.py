"""Merkle tree construction and inclusion-proof verification."""

from __future__ import annotations

from src.crypto.hash_utils import hash_text


def build_merkle_root(tx_ids: list[str]) -> str:
    """Build Merkle root from transaction ids.

    Leaves are defined as sha256(tx_id), and each parent as sha256(left + right).
    If a level has odd count, the last hash is duplicated.
    """
    if not tx_ids:
        return hash_text("")

    level = [hash_text(tx_id) for tx_id in tx_ids]
    while len(level) > 1:
        level = _build_next_level(level)

    return level[0]


def build_merkle_levels(tx_ids: list[str]) -> list[list[str]]:
    """Return all Merkle levels from leaves to root for proof generation."""
    if not tx_ids:
        empty = hash_text("")
        return [[empty]]

    levels: list[list[str]] = [[hash_text(tx_id) for tx_id in tx_ids]]
    while len(levels[-1]) > 1:
        levels.append(_build_next_level(levels[-1]))
    return levels


def get_merkle_proof(tx_ids: list[str], tx_index: int) -> list[tuple[str, str]]:
    """Build inclusion proof for a transaction index.

    Proof item format: (position, sibling_hash), where position is "left" or "right"
    from the perspective of the current node.
    """
    if tx_index < 0 or tx_index >= len(tx_ids):
        raise IndexError("tx_index out of range")

    levels = build_merkle_levels(tx_ids)
    proof: list[tuple[str, str]] = []
    index = tx_index

    for level in levels[:-1]:
        is_right_node = index % 2 == 1
        sibling_index = index - 1 if is_right_node else index + 1
        if sibling_index >= len(level):
            sibling_index = index
        sibling_hash = level[sibling_index]
        position = "left" if is_right_node else "right"
        proof.append((position, sibling_hash))
        index //= 2

    return proof


def verify_merkle_proof(tx_id: str, proof: list[tuple[str, str]], expected_root: str) -> bool:
    """Verify whether tx_id belongs to the Merkle tree with expected_root."""
    current = hash_text(tx_id)
    for position, sibling_hash in proof:
        if position == "left":
            current = hash_text(sibling_hash + current)
        elif position == "right":
            current = hash_text(current + sibling_hash)
        else:
            return False
    return current == expected_root


def _build_next_level(level: list[str]) -> list[str]:
    next_level: list[str] = []
    for i in range(0, len(level), 2):
        left = level[i]
        right = level[i + 1] if i + 1 < len(level) else level[i]
        next_level.append(hash_text(left + right))
    return next_level
