
from rate_limiter.sliding_window import SlidingWindow


def test_request_accepted():
    limiter = SlidingWindow(limit=3, window_seconds=10)

    result = limiter.acquire()

    assert result["allowed"] is True
    assert result["remaining"] == 2
    assert result["retry_after"] == 0


def test_request_rejected_when_limit_exhausted():
    limiter = SlidingWindow(limit=2, window_seconds=10)

    limiter.acquire()
    limiter.acquire()

    result = limiter.acquire()

    assert result["allowed"] is False
    assert result["remaining"] == 0
    assert result["retry_after"] > 0
