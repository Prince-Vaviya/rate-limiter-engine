class SimpleRateLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.requests = 0

    def acquire(self):
        if self.requests < self.limit:
            self.requests += 1
            return True

        return False


limiter = SimpleRateLimiter(limit=5)

for i in range(7):
    result = limiter.acquire()
    print(f"Request {i+1} : {result}")