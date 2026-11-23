import threading
from rate_limiter.state import StateManager
from rate_limiter.sliding_window import SlidingWindow
from rate_limiter.token_bucket import TokenBucket

class RateLimiter:

    def __init__(self):
        self.state_manager = StateManager()
        self.lock = threading.Lock()

    def configure(self, client_id, resource_id, strategy, capacity, **kwargs):
        key = (client_id, resource_id)

        if strategy == "sliding_window":
            limiter = SlidingWindow(capacity, kwargs["window_seconds"])

        else:
            limiter = TokenBucket(capacity, kwargs["refill_rate"])

        with self.lock:
            self.state_manager.create_state(client_id, resource_id, limiter)

    def acquire(self, client_id, resource_id):

        with self.lock:
            limiter = self.state_manager.get_state(client_id, resource_id)

        return limiter.acquire()

    def remove(self, client_id, resource_id):
        with self.lock:
            self.state_manager.remove_state(client_id, resource_id)