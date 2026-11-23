
from rate_limiter.token_bucket import TokenBucket


def test_request_accepted():
    limiter = TokenBucket(capacity=3, refill_rate=1)

    result = limiter.acquire()

    assert result["allowed"] is True
    assert result["remaining"] < 3
    assert result["retry_after"] == 0


def test_request_rejected_when_bucket_empty():
    limiter = TokenBucket(capacity=2, refill_rate=0.001)

    limiter.acquire()
    limiter.acquire()

    result = limiter.acquire()

    assert result["allowed"] is False
    assert result["remaining"] < 1
    assert result["retry_after"] > 0


def test_token_bucket_does_not_exceed_capacity():
    limiter = TokenBucket(capacity=5, refill_rate=1)

    result = limiter.acquire()

    assert result["allowed"] is True
    assert result["remaining"] <= 5
