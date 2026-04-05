from src.phase1.pipeline import (
    build_verifiable_merkle_bundle,
    create_account,
    create_signed_siso_transaction,
)


def test_phase1_pipeline_creates_signed_siso_transactions_and_merkle_bundle():
    alice = create_account("Alice")
    bob = create_account("Bob")
    carol = create_account("Carol")

    tx1 = create_signed_siso_transaction(alice, bob, 5.0)
    tx2 = create_signed_siso_transaction(bob, carol, 2.0)
    tx3 = create_signed_siso_transaction(alice, carol, 1.0)

    bundle = build_verifiable_merkle_bundle([tx1, tx2, tx3])

    assert len(bundle["tx_ids"]) == 3
    assert len(bundle["merkle_root"]) == 64
    assert all(item["verified"] for item in bundle["proofs"])
