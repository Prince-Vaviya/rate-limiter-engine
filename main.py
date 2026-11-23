import time
from rate_limiter.sliding_window import SlidingWindow

limiter = SlidingWindow(3, 10)

for i in range(4):
    print(limiter.acquire())