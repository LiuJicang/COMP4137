"""Transaction model for SISO transfer."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from src.crypto.hash_utils import hash_json
from src.crypto.signature import sign_message, verify_signature


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
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
        signature = sign_message(self.tx_id.encode("utf-8"), private_pem)
        self.signature_hex = signature.hex()

    def verify(self, sender_public_pem: str) -> bool:
        expected_tx_id = self.compute_tx_id()
        if self.tx_id and self.tx_id != expected_tx_id:
            return False
        if not self.signature_hex:
            return False
        return verify_signature(
            expected_tx_id.encode("utf-8"),
            bytes.fromhex(self.signature_hex),
            sender_public_pem,
        )
