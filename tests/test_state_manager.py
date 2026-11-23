
from rate_limiter.limiter import RateLimiter


def test_state_manager():

    limiter = RateLimiter()

    # 1. Create state
    limiter.configure(
        client_id="client_A",
        resource_id="llm-v1",
        strategy="token_bucket",
        capacity=5,
        refill_rate=1
    )

    manager = limiter.state_manager

    # 2. Verify creation
    assert manager.has_state("client_A", "llm-v1")

    # 3. Retrieve state
    state = manager.get_state("client_A", "llm-v1")
    assert state is not None

    # 4. Remove state
    limiter.remove("client_A", "llm-v1")

    # 5. Verify removal
    assert not manager.has_state("client_A", "llm-v1")

    print("State Manager tests passed!")


if __name__ == "__main__":
    test_state_manager()
