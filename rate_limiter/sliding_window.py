from collections import deque
import time

class SlidingWindow:

    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window_seconds = window_seconds
        self.requests = deque()

    def acquire(self):
        now = time.monotonic()
        cutoff = now - self.window_seconds

        while self.requests and self.requests[0] <= cutoff:
            self.requests.popleft()

        remaining = self.limit - len(self.requests)

        if remaining == 0:
            retry_after = (
                self.requests[0] + self.window_seconds - now
            )

            return {
                "allowed": False,
                "remaining": 0,
                "retry_after": retry_after
            }

        self.requests.append(now)

        return {
            "allowed": True,
            "remaining": remaining - 1,
            "retry_after": 0
        }