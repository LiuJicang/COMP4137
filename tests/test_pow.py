from src.models.block import Block


def test_mining_finds_valid_hash_prefix():
    block = Block(
        index=1,
        previous_hash="0" * 64,
        merkle_root="abc123",
        transactions=[],
        difficulty=2,
    )
    block.mine()
    assert block.block_hash.startswith("00")
