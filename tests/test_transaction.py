import pytest

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
    assert tx.verify()


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


def test_transaction_record_round_trip_preserves_signature_and_sender_key():
    private_key, public_key = generate_key_pair()
    _, recipient_public = generate_key_pair()

    tx = Transaction(
        sender=address_from_public_key(public_key),
        recipient=address_from_public_key(recipient_public),
        amount=5.5,
    )
    tx.sign(private_key)

    record = tx.to_record()
    restored = Transaction.from_record(record)

    assert "sender_public_key" in record
    assert "signature_hex" in record
    assert restored.verify()
    assert restored.tx_id == tx.tx_id


def test_transaction_sign_fails_when_sender_does_not_match_signing_key():
    private_key, _ = generate_key_pair()
    _, recipient_public = generate_key_pair()

    tx = Transaction(
        sender="not_the_real_sender_address",
        recipient=address_from_public_key(recipient_public),
        amount=1.0,
    )

    with pytest.raises(ValueError):
        tx.sign(private_key)
