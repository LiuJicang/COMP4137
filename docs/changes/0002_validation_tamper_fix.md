# 0002 Validation Tamper Fix

- Date: 2026-04-05
- Owner: Integrity validation update

## Scope

- Updated `src/verification/validator.py`
- Updated `docs/changes/CHANGELOG.md`

## Why

Initial validation only checked block header hash and PoW. If transaction body changed without updating header data, tampering could go undetected.

## What Changed

- Recompute each transaction ID from transaction payload (`sender`, `recipient`, `amount`, `timestamp`).
- Rebuild Merkle root from recomputed IDs during chain validation.
- Fail validation if recomputed root differs from stored `merkle_root`.

## Verification

- Expected result after fix: tampering in an early block changes recomputed Merkle root and causes `is_chain_valid` to return `False`.

## Next

- Add negative tests for malformed transaction dicts.
- Add report screenshot from this tampering scenario.
