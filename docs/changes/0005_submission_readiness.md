# 0005 Submission Readiness

- Date: 2026-04-23
- Owner: final submission hardening pass

## Scope

- Updated `src/crypto/keys.py`
- Updated `src/models/transaction.py`
- Updated `src/models/blockchain.py`
- Updated `src/verification/validator.py`
- Updated `src/verification/tamper_demo.py`
- Updated `src/main.py`
- Updated `tests/test_transaction.py`
- Updated `tests/test_blockchain.py`
- Updated `tests/test_validation.py`
- Updated `scripts/run_demo.ps1`
- Updated `README.md`
- Updated `docs/video_script.md`
- Added `docs/report_assets/final_report_draft.md`
- Added `docs/report_assets/submission_checklist.md`

## Why

The GitHub repository had not changed since 2026-04-05 and still looked closer to a scaffold than a final submission package. The main risks were incomplete transaction verification at chain-validation time, a demo that showed only one mined block, and missing final-report support materials.

## What Changed

- Stored sender public keys and signatures in block transaction records so chain validation can re-verify signed transactions instead of checking only hashes.
- Strengthened validation to check genesis consistency, block hashes, PoW, transaction signatures, and Merkle roots.
- Expanded the main demo to mine two non-genesis blocks and print a clearer chain summary.
- Added tests for transaction serialization, sender/key mismatch handling, stored block transaction data, and signature tampering.
- Updated reproducibility instructions and added report/video submission support documents.

## Verification

- Run `python -m pip install -r requirements.txt`
- Run `python -m pytest -q`
- Run `python -m src.phase1_demo`
- Run `python -m src.main`

## Next

- Replace the contribution placeholders in the report draft with real team member names.
- Capture final screenshots from the passing tests and demo runs for the report and video.
