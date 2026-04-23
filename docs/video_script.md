# Video Script (5 minutes)

## Segment 1 (0:00 - 0:35): Team and goal

- Introduce the team and state each member's main contribution.
- State the goal: build a mini blockchain with signed transactions, Merkle verification, PoW mining, and tamper detection.

## Segment 2 (0:35 - 1:30): Phase I demo

- Run `python -m src.phase1_demo`.
- Show generated accounts and explain address derivation.
- Show signed SISO transactions with transaction IDs.
- Show the Merkle root and inclusion proof verification results.

## Segment 3 (1:30 - 3:00): Phase II demo

- Run `python -m src.main`.
- Explain the genesis block and the two mined non-genesis blocks.
- Point out the previous hash linkage, nonce, block hash, and Merkle root shown in the console.
- Mention that transaction signatures are stored in block records and re-verified during validation.

## Segment 4 (3:00 - 4:15): Integrity verification and tamper attack

- Show that the chain is valid before tampering.
- Explain that one transaction amount in an existing block is modified manually by the tamper demo.
- Re-run validation and show that the chain becomes invalid.
- State why it fails: the modified transaction no longer matches its signature and the recomputed Merkle root no longer matches the block record.

## Segment 5 (4:15 - 5:00): Reproducibility and conclusion

- Show `python -m pytest -q`.
- Mention the README setup steps and the reproducibility helper script.
- Close with one sentence on what the project demonstrates about blockchain integrity.
