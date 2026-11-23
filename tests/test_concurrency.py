import threading
from concurrent.futures import ThreadPoolExecutor
from rate_limiter.limiter import RateLimiter


def test_concurrent_requests():

    limiter = RateLimiter()

    limiter.configure(
        client_id="client_A",
        resource_id="llm-v1",
        strategy="token_bucket",
        capacity=10,
        refill_rate=0.001
    )

    def send_request():
        return limiter.acquire("client_A", "llm-v1")

    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(
            executor.map(
                lambda _: send_request(),
                range(100)
            )
        )

    accepted = sum(
        1 for result in results if result["allowed"]
    )

    rejected = sum(
        1 for result in results if not result["allowed"]
    )

    print("Accepted:", accepted)
    print("Rejected:", rejected)

    assert accepted == 10
    assert rejected == 90


if __name__ == "__main__":
    test_concurrent_requests()
