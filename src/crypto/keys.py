"""Keypair generation and address derivation."""

from __future__ import annotations

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from src.crypto.hash_utils import hash_text


def generate_key_pair() -> tuple[str, str]:
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")

    return private_pem, public_pem


def public_key_from_pem(public_pem: str):
    return serialization.load_pem_public_key(public_pem.encode("utf-8"))


def private_key_from_pem(private_pem: str):
    return serialization.load_pem_private_key(private_pem.encode("utf-8"), password=None)


def public_pem_from_private_pem(private_pem: str) -> str:
    private_key = private_key_from_pem(private_pem)
    public_key = private_key.public_key()
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")


def address_from_public_key(public_pem: str) -> str:
    # Compact deterministic address for demo use.
    return hash_text(public_pem)[:40]
