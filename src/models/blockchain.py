"""Blockchain container and block append logic."""

from __future__ import annotations

from src.config import DEFAULT_DIFFICULTY
from src.crypto.hash_utils import hash_text
from src.merkle.tree import build_merkle_root
from src.models.block import Block
from src.models.transaction import Transaction


class Blockchain:
    def __init__(self, difficulty: int = DEFAULT_DIFFICULTY) -> None:
        self.difficulty = difficulty
        self.chain: list[Block] = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        genesis = Block(
            index=0,
            previous_hash="0" * 64,
            merkle_root=hash_text("genesis"),
            transactions=[{"genesis": True}],
            difficulty=self.difficulty,
        )
        genesis.mine()
        return genesis

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, transactions: list[Transaction]) -> Block:
        tx_records: list[dict] = []
        tx_ids: list[str] = []
        for tx in transactions:
            if not tx.verify():
                raise ValueError("Cannot add unsigned or invalid transaction to a block")
            tx_record = tx.to_record()
            tx_records.append(tx_record)
            tx_ids.append(tx_record["tx_id"])

        block = Block(
            index=len(self.chain),
            previous_hash=self.last_block.block_hash,
            merkle_root=build_merkle_root(tx_ids),
            transactions=tx_records,
            difficulty=self.difficulty,
        )
        block.mine()
        self.chain.append(block)
        return block
