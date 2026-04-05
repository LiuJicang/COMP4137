from src.crypto.keys import address_from_public_key, generate_key_pair
from src.models.blockchain import Blockchain
from src.models.transaction import Transaction


def test_block_links_previous_hash_correctly():
    private_key, public_key = generate_key_pair()
    _, recipient_public = generate_key_pair()

    tx = Transaction(
        sender=address_from_public_key(public_key),
        recipient=address_from_public_key(recipient_public),
        amount=1.0,
    )
    tx.sign(private_key)

    chain = Blockchain(difficulty=2)
    new_block = chain.add_block([tx])
    assert new_block.previous_hash == chain.chain[0].block_hash
