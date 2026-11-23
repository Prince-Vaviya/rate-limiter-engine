import time
from rate_limiter.token_bucket import TokenBucket

limiter = TokenBucket(3, 0.5)

for i in range(4):
    print(limiter.acquire())