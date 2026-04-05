from src.merkle.tree import build_merkle_root


def test_merkle_root_is_deterministic_for_same_input():
    tx_ids = ["tx1", "tx2", "tx3", "tx4"]
    root1 = build_merkle_root(tx_ids)
    root2 = build_merkle_root(tx_ids)
    assert root1 == root2
