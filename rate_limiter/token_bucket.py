import time

class TokenBucket:

    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate  # refill rate per second

        self.tokens = capacity
        self.last_refill = time.monotonic()


    def acquire(self):
        now = time.monotonic()

        elapsed = now - self.last_refill

        self.tokens = min(
            self.capacity,
            self.tokens + elapsed * self.refill_rate
        )

        self.last_refill = now

        if self.tokens >= 1:
            self.tokens -= 1
            return {
                "allowed": True,
                "remaining": self.tokens,
                "retry_after": 0
            }

        retry_after = (1 - self.tokens) / self.refill_rate

        return {
                "allowed": False,
                "remaining": self.tokens,
                "retry_after": retry_after
            }