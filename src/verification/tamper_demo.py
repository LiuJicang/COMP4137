"""Tampering simulation for integrity verification."""

from __future__ import annotations

from src.models.blockchain import Blockchain
from src.verification.validator import is_chain_valid


def simulate_tamper_and_validate(blockchain: Blockchain) -> tuple[bool, bool]:
    before = is_chain_valid(blockchain)
    if len(blockchain.chain) > 1:
        target = blockchain.chain[1]
        if target.transactions and isinstance(target.transactions[0], dict):
            target.transactions[0]["amount"] = 999999
    after = is_chain_valid(blockchain)
    return before, after
