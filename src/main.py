"""Demo entry point for mini blockchain flow."""

from __future__ import annotations

from src.crypto.keys import address_from_public_key, generate_key_pair
from src.models.blockchain import Blockchain
from src.models.transaction import Transaction
from src.verification.tamper_demo import simulate_tamper_and_validate
from src.verification.validator import is_chain_valid


def build_demo_chain() -> Blockchain:
    alice_private, alice_public = generate_key_pair()
    bob_private, bob_public = generate_key_pair()
    _, carol_public = generate_key_pair()

    alice_addr = address_from_public_key(alice_public)
    bob_addr = address_from_public_key(bob_public)
    carol_addr = address_from_public_key(carol_public)

    tx1 = Transaction(sender=alice_addr, recipient=bob_addr, amount=12.5)
    tx1.sign(alice_private)
    assert tx1.verify(alice_public)

    tx2 = Transaction(sender=bob_addr, recipient=carol_addr, amount=4.0)
    tx2.sign(bob_private)
    assert tx2.verify(bob_public)

    tx3 = Transaction(sender=alice_addr, recipient=carol_addr, amount=2.25)
    tx3.sign(alice_private)
    assert tx3.verify(alice_public)

    chain = Blockchain(difficulty=3)
    chain.add_block([tx1, tx2])
    chain.add_block([tx3])
    return chain


def main() -> None:
    chain = build_demo_chain()

    print("=== Mini Blockchain Demo ===")
    print("[1] Chain valid before tamper:", is_chain_valid(chain))
    print("[2] Chain summary:")
    for block in chain.chain:
        print(
            f"    Block {block.index}: tx_count={len(block.transactions)} nonce={block.nonce} "
            f"hash={block.block_hash[:16]}... merkle={block.merkle_root[:16]}..."
        )

    before, after = simulate_tamper_and_validate(chain)
    print("[3] Tamper demo (before, after):", before, after)
    print("[4] Chain length:", len(chain.chain))
    print("[5] Latest block hash:", chain.last_block.block_hash)


if __name__ == "__main__":
    main()
