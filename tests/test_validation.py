from src.main import build_demo_chain
from src.verification.tamper_demo import simulate_tamper_and_validate
from src.verification.validator import is_chain_valid


def test_chain_valid_then_invalid_after_tamper():
    chain = build_demo_chain()
    assert is_chain_valid(chain)
    before, after = simulate_tamper_and_validate(chain)
    assert before is True
    assert after is False
