"""Demo entry point for mini blockchain flow."""

from __future__ import annotations

from src.crypto.keys import address_from_public_key, generate_key_pair
from src.models.blockchain import Blockchain
from src.models.transaction import Transaction
from src.verification.tamper_demo import simulate_tamper_and_validate
from src.verification.validator import is_chain_valid


def build_demo_chain() -> Blockchain:
    alice_private, alice_public = generate_key_pair()
    _, bob_public = generate_key_pair()

    alice_addr = address_from_public_key(alice_public)
    bob_addr = address_from_public_key(bob_public)

    tx = Transaction(sender=alice_addr, recipient=bob_addr, amount=12.5)
    tx.sign(alice_private)
    assert tx.verify(alice_public)

    chain = Blockchain(difficulty=4)
    chain.add_block([tx])
    return chain


def main() -> None:
    chain = build_demo_chain()

    print("[1] Chain valid before tamper:", is_chain_valid(chain))
    before, after = simulate_tamper_and_validate(chain)
    print("[2] Tamper demo (before, after):", before, after)
    print("[3] Chain length:", len(chain.chain))
    print("[4] Latest block hash:", chain.last_block.block_hash)


if __name__ == "__main__":
    main()
