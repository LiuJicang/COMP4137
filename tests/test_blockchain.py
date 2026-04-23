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


def test_block_stores_verifiable_transaction_record():
    private_key, public_key = generate_key_pair()
    _, recipient_public = generate_key_pair()

    tx = Transaction(
        sender=address_from_public_key(public_key),
        recipient=address_from_public_key(recipient_public),
        amount=2.5,
    )
    tx.sign(private_key)

    chain = Blockchain(difficulty=2)
    new_block = chain.add_block([tx])
    stored_tx = new_block.transactions[0]

    assert stored_tx["tx_id"] == tx.tx_id
    assert stored_tx["signature_hex"] == tx.signature_hex
    assert stored_tx["sender_public_key"] == tx.sender_public_key
