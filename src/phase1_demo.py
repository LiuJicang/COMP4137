"""Standalone demo script for Phase I deliverables."""

from __future__ import annotations

from src.phase1.pipeline import (
    build_verifiable_merkle_bundle,
    create_account,
    create_signed_siso_transaction,
)


def main() -> None:
    alice = create_account("Alice")
    bob = create_account("Bob")
    carol = create_account("Carol")

    tx1 = create_signed_siso_transaction(alice, bob, 10.0)
    tx2 = create_signed_siso_transaction(bob, carol, 4.5)
    tx3 = create_signed_siso_transaction(alice, carol, 1.25)
    txs = [tx1, tx2, tx3]

    bundle = build_verifiable_merkle_bundle(txs)

    print("=== Phase I Demo ===")
    print("Generated accounts:")
    print("-", alice.owner, alice.address)
    print("-", bob.owner, bob.address)
    print("-", carol.owner, carol.address)

    print("\nSigned transactions:")
    for tx in txs:
        print(f"- tx_id={tx.compute_tx_id()} sender={tx.sender} recipient={tx.recipient} amount={tx.amount}")

    print("\nMerkle root:", bundle["merkle_root"])
    print("Inclusion proof verification:")
    for item in bundle["proofs"]:
        print(f"- {item['tx_id'][:16]}... verified={item['verified']}")


if __name__ == "__main__":
    main()
