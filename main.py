import time
from rate_limiter.limiter import RateLimiter

limiter = RateLimiter()

# This is client A configuration
limiter.configure(
    client_id = "client_A",
    resource_id = "llm-v1",
    strategy = "sliding_window",
    capacity = 3,
    window_seconds = 10
)

# This is client B configuration
limiter.configure(
    client_id = "client_B",
    resource_id = "llm-v1",
    strategy = "token_bucket",
    capacity = 5,
    refill_rate = 1
)

for i in range(4):
    print("Client A:", limiter.acquire("client_A", "llm-v1"))

for i in range(6):
    print("Client B:", limiter.acquire("client_B", "llm-v1"))