"""Transaction model for SISO transfer."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.crypto.hash_utils import hash_json
from src.crypto.keys import address_from_public_key, public_pem_from_private_pem
from src.crypto.signature import sign_message, verify_signature


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    sender_public_key: str = ""
    signature_hex: str = ""
    tx_id: str = ""

    def payload(self) -> dict:
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }

    def compute_tx_id(self) -> str:
        return hash_json(self.payload())

    def sign(self, private_pem: str) -> None:
        self.tx_id = self.compute_tx_id()
        self.sender_public_key = public_pem_from_private_pem(private_pem)
        if self.sender != address_from_public_key(self.sender_public_key):
            raise ValueError("Sender address does not match the signing key")
        signature = sign_message(self.tx_id.encode("utf-8"), private_pem)
        self.signature_hex = signature.hex()

    def verify(self, sender_public_pem: str | None = None) -> bool:
        public_key = sender_public_pem or self.sender_public_key
        expected_tx_id = self.compute_tx_id()
        if self.tx_id and self.tx_id != expected_tx_id:
            return False
        if not self.signature_hex or not public_key:
            return False
        if self.sender != address_from_public_key(public_key):
            return False
        try:
            signature = bytes.fromhex(self.signature_hex)
        except ValueError:
            return False
        return verify_signature(expected_tx_id.encode("utf-8"), signature, public_key)

    def to_record(self) -> dict[str, Any]:
        if not self.verify():
            raise ValueError("Cannot serialize an unsigned or invalid transaction")
        return {
            **self.payload(),
            "sender_public_key": self.sender_public_key,
            "signature_hex": self.signature_hex,
            "tx_id": self.tx_id or self.compute_tx_id(),
        }

    @classmethod
    def from_record(cls, record: dict[str, Any]) -> "Transaction":
        return cls(
            sender=record.get("sender", ""),
            recipient=record.get("recipient", ""),
            amount=record.get("amount", 0.0),
            timestamp=record.get("timestamp", ""),
            sender_public_key=record.get("sender_public_key", ""),
            signature_hex=record.get("signature_hex", ""),
            tx_id=record.get("tx_id", ""),
        )
