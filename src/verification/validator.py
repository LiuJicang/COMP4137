"""Chain validation logic."""

from __future__ import annotations

from src.crypto.hash_utils import hash_text
from src.merkle.tree import build_merkle_root
from src.mining.pow import meets_difficulty
from src.models.block import Block
from src.models.blockchain import Blockchain
from src.models.transaction import Transaction


def is_chain_valid(blockchain: Blockchain) -> bool:
    chain = blockchain.chain
    for i, current in enumerate(chain):
        if not _is_hash_and_pow_valid(current):
            return False

        if i == 0:
            if current.previous_hash != "0" * 64:
                return False
            if current.merkle_root != hash_text("genesis"):
                return False
            continue

        current = chain[i]
        previous = chain[i - 1]

        if current.previous_hash != previous.block_hash:
            return False

        tx_ids: list[str] = []
        for tx in current.transactions:
            if not _is_transaction_record_valid(tx):
                return False
            tx_ids.append(tx["tx_id"])

        expected_merkle = build_merkle_root(tx_ids)
        if current.merkle_root != expected_merkle:
            return False

    return True


def _is_hash_and_pow_valid(block: Block) -> bool:
    if block.calculate_hash() != block.block_hash:
        return False
    return meets_difficulty(block.block_hash, block.difficulty)


def _is_transaction_record_valid(record: object) -> bool:
    if not isinstance(record, dict):
        return False
    tx = Transaction.from_record(record)
    if not tx.verify():
        return False
    return record.get("tx_id") == tx.compute_tx_id()
