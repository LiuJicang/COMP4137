# Mini Blockchain Project (COMP4137/COMP7200)

This repository contains a Python implementation scaffold for the course programming project: **Implementation of a Mini Blockchain**.

## 1. Project Goal

Build a compact but functional blockchain system that demonstrates:

- Account creation with public/private keys
- Signed SISO (single-input-single-output) transactions
- Verifiable Merkle tree construction from transactions
- Block and chain construction
- Proof-of-Work (PoW) mining
- Chain integrity verification and tampering detection

## 2. Scope and Key Points

This project intentionally focuses on the required core features only.

- Included: transactions, Merkle root, blockchain, PoW, integrity verification, reproducibility artifacts
- Excluded: P2P networking, smart contracts, wallets UI, distributed consensus cluster

## 3. Recommended Workflow

1. Complete Phase I core modules first (transaction + Merkle tree).
2. Integrate Phase II modules (chain + mining + validation).
3. Keep tests, README, and report assets updated in parallel.

## 4. Team of Four: Suggested Ownership

- Member A: `src/crypto/`, `src/models/transaction.py`, `tests/test_transaction.py`
- Member B: `src/merkle/`, `src/models/block.py`, `tests/test_merkle.py`
- Member C: `src/models/blockchain.py`, `src/mining/`, `tests/test_pow.py`, `tests/test_blockchain.py`
- Member D: `src/verification/`, `tests/test_validation.py`, `README/docs/video/report integration`

Cross-stage rule:

- A or B must join Phase II integration.
- C or D must review and improve Phase I tests/docs.

## 5. Repository Structure

```text
group/
  src/
    config.py
    main.py
    crypto/
      hash_utils.py
      keys.py
      signature.py
    merkle/
      tree.py
    mining/
      pow.py
    models/
      transaction.py
      block.py
      blockchain.py
    verification/
      validator.py
      tamper_demo.py
  tests/
    test_transaction.py
    test_merkle.py
    test_blockchain.py
    test_pow.py
    test_validation.py
  scripts/
    run_demo.ps1
    run_demo.sh
  docs/
    video_script.md
    report_assets/
    changes/
      CHANGELOG.md
      README.md
      0001_initial_scaffold.md
  requirements.txt
  .gitignore
  README.md
```

## 6. Environment and Installation

Recommended:

- Python 3.10+
- Windows/macOS/Linux

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## 7. Run the Demo

Main demo:

```bash
python -m src.main
```

Run tests:

```bash
pytest -q
```

PowerShell helper:

```powershell
./scripts/run_demo.ps1
```

## 8. Phase Mapping

- Phase I: `crypto`, `transaction`, `merkle`, plus related tests
- Phase II: `block`, `blockchain`, `pow`, `validator`, `tamper_demo`, plus related tests
- Final submission: README polishing, report assets in `docs/report_assets/`, video script in `docs/video_script.md`

## 9. Reproducibility Checklist

- Pin dependencies in `requirements.txt`
- Keep deterministic test cases in `tests/`
- Record every notable change in `docs/changes/`
- Ensure demo output is consistent with report screenshots

## 10. Change Tracking Policy

All meaningful modifications must be documented under `docs/changes/`:

- Append one summary line in `docs/changes/CHANGELOG.md`
- Add one detailed file per change batch using numbered pattern
- Use `docs/changes/README.md` template to keep entries consistent
