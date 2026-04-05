"""ECDSA signing and verification utilities."""

from __future__ import annotations

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from src.crypto.keys import private_key_from_pem, public_key_from_pem


def sign_message(message: bytes, private_pem: str) -> bytes:
    private_key = private_key_from_pem(private_pem)
    return private_key.sign(message, ec.ECDSA(hashes.SHA256()))


def verify_signature(message: bytes, signature: bytes, public_pem: str) -> bool:
    public_key = public_key_from_pem(public_pem)
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False
