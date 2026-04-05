"""Hash helpers used across modules."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def hash_text(text: str) -> str:
    return sha256_hex(text.encode("utf-8"))


def hash_json(data: Any) -> str:
    payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hash_text(payload)
