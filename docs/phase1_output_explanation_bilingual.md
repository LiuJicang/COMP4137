# Phase I Output Explanation and Summary

This file is a submission-safe reference note for the Phase I deliverable. The exact addresses, transaction IDs, and Merkle root will change on each run because fresh key pairs are generated every time, but the output structure should remain the same.

## 1. Representative Output Format

```text
python -m src.phase1_demo
=== Phase I Demo ===
Generated accounts:
- Alice <address>
- Bob <address>
- Carol <address>

Signed transactions:
- tx_id=<hash> sender=<address> recipient=<address> amount=10.0
- tx_id=<hash> sender=<address> recipient=<address> amount=4.5
- tx_id=<hash> sender=<address> recipient=<address> amount=1.25

Merkle root: <merkle_root>
Inclusion proof verification:
- <tx_id_prefix>... verified=True
- <tx_id_prefix>... verified=True
- <tx_id_prefix>... verified=True
```

## 2. Explanation of Output

1. `Generated accounts`

- This section shows that the system successfully creates accounts, key pairs, and addresses derived from the public keys.

2. `Signed transactions`

- Each transaction includes `tx_id`, `sender`, `recipient`, and `amount`.
- This demonstrates the SISO transaction structure and deterministic transaction ID computation from the transaction payload.
- Transactions are signed and verified before being displayed.

3. `Merkle root`

- A 64-character hexadecimal hash is printed, showing that the transaction list has been aggregated into a Merkle tree and summarized by a single root hash.

4. `Inclusion proof verification`

- Every transaction is reported as `verified=True`, which means each transaction can be proven to belong to the same Merkle tree.
- This satisfies the core requirement of a verifiable Merkle tree.

## 3. Summary

This output is valid evidence that Phase I has been completed successfully:

- account creation works
- SISO transaction generation works
- transaction hashing works
- signature and verification work
- Merkle root construction works
- inclusion proof verification works
