"""Chain validation logic."""

from __future__ import annotations

from src.crypto.hash_utils import hash_json
from src.merkle.tree import build_merkle_root
from src.mining.pow import meets_difficulty
from src.models.blockchain import Blockchain


def is_chain_valid(blockchain: Blockchain) -> bool:
    chain = blockchain.chain
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]

        if current.previous_hash != previous.block_hash:
            return False
        if current.calculate_hash() != current.block_hash:
            return False
        if not meets_difficulty(current.block_hash, current.difficulty):
            return False

        tx_ids: list[str] = []
        for tx in current.transactions:
            if not isinstance(tx, dict):
                return False
            tx_payload = {
                "sender": tx.get("sender"),
                "recipient": tx.get("recipient"),
                "amount": tx.get("amount"),
                "timestamp": tx.get("timestamp"),
            }
            tx_ids.append(hash_json(tx_payload))

        expected_merkle = build_merkle_root(tx_ids)
        if current.merkle_root != expected_merkle:
            return False

    return True
