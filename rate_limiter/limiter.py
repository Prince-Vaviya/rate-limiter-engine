from rate_limiter.sliding_window import SlidingWindow
from rate_limiter.token_bucket import TokenBucket

class RateLimiter:

    def __init__(self):
        self.clients = {}

    def configure(self, client_id, resource_id, strategy, capacity, **kwargs):
        key = (client_id, resource_id)

        if strategy == "sliding_window":
            limiter = SlidingWindow(capacity, kwargs["window_seconds"])

        else:
            limiter = TokenBucket(capacity, kwargs["refill_rate"])

        self.clients[key] = limiter

    def acquire(self, client_id, resource_id):

        key = (client_id, resource_id)

        if key not in self.clients:
            raise ValueError("Client/resource not valid")

        return self.clients[key].acquire()