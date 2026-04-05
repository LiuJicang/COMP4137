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
        tx_ids = [tx.compute_tx_id() for tx in transactions]
        tx_payloads = [tx.payload() | {"tx_id": tx.compute_tx_id()} for tx in transactions]
        block = Block(
            index=len(self.chain),
            previous_hash=self.last_block.block_hash,
            merkle_root=build_merkle_root(tx_ids),
            transactions=tx_payloads,
            difficulty=self.difficulty,
        )
        block.mine()
        self.chain.append(block)
        return block
