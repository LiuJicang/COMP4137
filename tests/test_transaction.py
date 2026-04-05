from src.crypto.keys import address_from_public_key, generate_key_pair
from src.models.transaction import Transaction


def test_transaction_sign_and_verify_success():
    private_key, public_key = generate_key_pair()
    _, recipient_public = generate_key_pair()

    tx = Transaction(
        sender=address_from_public_key(public_key),
        recipient=address_from_public_key(recipient_public),
        amount=7.25,
    )
    tx.sign(private_key)
    assert tx.verify(public_key)


def test_transaction_verify_fails_after_tamper():
    private_key, public_key = generate_key_pair()
    _, recipient_public = generate_key_pair()

    tx = Transaction(
        sender=address_from_public_key(public_key),
        recipient=address_from_public_key(recipient_public),
        amount=3.0,
    )
    tx.sign(private_key)
    tx.amount = 9.0
    assert not tx.verify(public_key)
