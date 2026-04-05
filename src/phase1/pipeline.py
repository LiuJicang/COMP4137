"""High-level workflow for project Phase I requirements."""

from __future__ import annotations

from dataclasses import dataclass

from src.crypto.keys import address_from_public_key, generate_key_pair
from src.merkle.tree import build_merkle_root, get_merkle_proof, verify_merkle_proof
from src.models.transaction import Transaction


@dataclass
class Account:
    owner: str
    private_key_pem: str
    public_key_pem: str
    address: str


def create_account(owner: str) -> Account:
    private_key, public_key = generate_key_pair()
    return Account(
        owner=owner,
        private_key_pem=private_key,
        public_key_pem=public_key,
        address=address_from_public_key(public_key),
    )


def create_signed_siso_transaction(sender: Account, recipient: Account, amount: float) -> Transaction:
    tx = Transaction(sender=sender.address, recipient=recipient.address, amount=amount)
    tx.sign(sender.private_key_pem)
    if not tx.verify(sender.public_key_pem):
        raise ValueError("Transaction signature verification failed")
    return tx


def build_verifiable_merkle_bundle(transactions: list[Transaction]) -> dict:
    tx_ids = [tx.compute_tx_id() for tx in transactions]
    merkle_root = build_merkle_root(tx_ids)

    proofs: list[dict] = []
    for idx, tx in enumerate(transactions):
        proof = get_merkle_proof(tx_ids, idx)
        verified = verify_merkle_proof(tx.compute_tx_id(), proof, merkle_root)
        proofs.append(
            {
                "tx_id": tx.compute_tx_id(),
                "proof": proof,
                "verified": verified,
            }
        )

    return {
        "tx_ids": tx_ids,
        "merkle_root": merkle_root,
        "proofs": proofs,
    }
