# Mini Blockchain Project (COMP4137/COMP7200)

This repository contains a compact, course-focused implementation of a mini blockchain. The codebase is designed to satisfy the programming requirements for account creation, signed SISO transactions, verifiable Merkle trees, block and chain construction, Proof-of-Work mining, and integrity validation with tamper detection.

## 1. Project Information

- Title: Implementation of a Mini Blockchain
- Group Number: `<fill in group number>`
- Members:
  - `<Member 1 name, student ID>`
  - `<Member 2 name, student ID>`
  - `<Member 3 name, student ID>`
  - `<Member 4 name, student ID>`

## 2. Implemented Features

- Public/private key account generation with deterministic demo addresses
- Signed SISO transactions with transaction IDs derived from transaction payloads
- Verifiable Merkle tree construction with inclusion proofs
- Genesis block plus linked blockchain growth
- Configurable Proof-of-Work mining based on leading-zero difficulty
- Full chain validation covering block hashes, PoW, Merkle roots, and transaction signatures
- Tamper simulation showing that modified block data is detected immediately

## 3. Abstract and Artifact Role

This artifact contains the full implementation of a mini blockchain system used to reproduce the main outcomes described in the report. The artifact demonstrates account creation, signed transactions, Merkle root construction, block mining, chain validation, and attack detection. Its role is to provide executable evidence that the reported system works as described and that the observed results can be reproduced by the marker.

## 4. Repository Structure

```text
src/
  config.py
  main.py
  phase1_demo.py
  crypto/
  merkle/
  mining/
  models/
  phase1/
  verification/
tests/
scripts/
docs/
  video_script.md
  report_assets/
  changes/
```

## 5. Dependencies and Requirements

- Python 3.10 or newer
- Windows, macOS, or Linux
- Recommended hardware: any modern laptop or desktop with at least 4 GB RAM

Main dependency:

- `cryptography`

Test dependency:

- `pytest`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

If `python` is not available on your machine, use the full interpreter path instead. For example on this workstation:

```powershell
D:\Anaconda\python.exe -m pip install -r requirements.txt
```

## 6. Installation and Deployment

Estimated installation time: 1 to 3 minutes.

1. Download or extract the project into a local directory.
2. Open a terminal in the project root.
3. Install the dependencies with `python -m pip install -r requirements.txt`.
4. No additional deployment step is required because this project runs locally as a Python application.

## 7. How to Run

Run the Phase I demo:

```bash
python -m src.phase1_demo
```

Run the full blockchain demo:

```bash
python -m src.main
```

Run the test suite:

```bash
python -m pytest -q
```

PowerShell helper for a full reproducibility pass:

```powershell
./scripts/run_demo.ps1
```

Linux or macOS helper:

```bash
./scripts/run_demo.sh
```

## 8. Expected Demo Behaviour

`src.phase1_demo` should show:

- three generated accounts
- three signed SISO transactions
- one Merkle root
- inclusion proof verification results for every transaction

`src.main` should show:

- a valid chain before tampering
- at least two mined non-genesis blocks
- block summaries including nonce, hash, and Merkle root
- a failed validation result after one block is tampered with

Estimated execution time:

- Phase I demo: a few seconds
- full demo: a few seconds
- full test suite: under 1 minute on a typical machine

## 9. Reproducibility of Experiments

This repository supports the following reproducible workflow:

1. Install dependencies from `requirements.txt`.
2. Run `python -m pytest -q` to confirm the implementation passes the automated checks.
3. Run `python -m src.phase1_demo` to reproduce Phase I outputs.
4. Run `python -m src.main` to reproduce the blockchain, mining, and tampering experiment.

The expected results are:

- all automated tests pass
- Phase I outputs show successful transaction generation, Merkle root construction, and inclusion-proof verification
- the final demo shows a valid chain before tampering and an invalid chain after tampering

These results directly correspond to the evidence discussed in the final report.

## 10. Phase Mapping

- Phase I: `src/crypto/`, `src/models/transaction.py`, `src/merkle/`, `src/phase1/`
- Phase II: `src/models/block.py`, `src/models/blockchain.py`, `src/mining/`, `src/verification/`
- Final submission support: `README.md`, `docs/video_script.md`, `docs/report_assets/`, `docs/changes/`

## 11. Submission Checklist

- Source code is included in this repository.
- `requirements.txt` lists runtime and test dependencies.
- `README.md` provides setup, run commands, and expected outputs.
- Tests are located under `tests/`.
- Report drafting material is under `docs/report_assets/`.
- Video talking points are in `docs/video_script.md`.
- Change records are tracked under `docs/changes/`.

## 12. Reproducibility Notes

- Transaction IDs and block hashes are computed with SHA-256 helpers.
- The test suite covers transaction signing, Merkle proofs, blockchain linking, PoW, and validation failures after tampering.
- The default demo difficulty is chosen to keep the runtime practical for grading and screen recording.

## 13. Change Tracking Policy

All meaningful modifications should be documented in `docs/changes/`:

- append one summary line to `docs/changes/CHANGELOG.md`
- add one numbered detail file for the change batch
- record how the change was verified
