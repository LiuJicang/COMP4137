from src.merkle.tree import build_merkle_root, get_merkle_proof, verify_merkle_proof


def test_merkle_root_is_deterministic_for_same_input():
    tx_ids = ["tx1", "tx2", "tx3", "tx4"]
    root1 = build_merkle_root(tx_ids)
    root2 = build_merkle_root(tx_ids)
    assert root1 == root2


def test_merkle_proof_verification_success_for_each_leaf():
    tx_ids = ["tx_a", "tx_b", "tx_c", "tx_d", "tx_e"]
    root = build_merkle_root(tx_ids)

    for idx, tx_id in enumerate(tx_ids):
        proof = get_merkle_proof(tx_ids, idx)
        assert verify_merkle_proof(tx_id, proof, root)


def test_merkle_proof_verification_fails_for_modified_transaction():
    tx_ids = ["tx1", "tx2", "tx3", "tx4"]
    root = build_merkle_root(tx_ids)
    proof = get_merkle_proof(tx_ids, 1)
    assert not verify_merkle_proof("tx2_modified", proof, root)

