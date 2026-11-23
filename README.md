# Rate Limiter Engine

A Python-based rate limiter supporting **Sliding Window** and **Token Bucket** algorithms, with centralized state management and thread-safe request handling.

## Features

- Sliding Window rate limiting
- Token Bucket rate limiting
- Per-client and per-resource rate-limit configuration
- Centralized state management
- Thread-safe request handling
- Request metadata: allowed status, remaining capacity, and retry delay
- Automated tests using pytest

## Project Structure

```text
rate-limiter-engine/
├── rate_limiter/
│   ├── __init__.py
│   ├── sliding_window.py
│   ├── token_bucket.py
│   ├── limiter.py
│   └── state.py
├── tests/
│   ├── test_sliding_window.py
│   ├── test_token_bucket.py
│   ├── test_state_manager.py
│   └── test_concurrency.py
├── pyproject.toml
└── README.md
```

## Rate Limiting Algorithms

### 1. Sliding Window

Tracks request timestamps within a configurable time window.

- Expired timestamps are removed.
- Requests are accepted while the limit is not exceeded.
- Rejected requests receive a retry delay.

### 2. Token Bucket

Maintains a bucket of tokens that refill over time.

- Each accepted request consumes one token.
- Tokens refill at a configured rate.
- Requests are rejected when fewer than one token is available.

## Architecture

The engine consists of three main layers:

1. **RateLimiter:** Public interface for configuring and acquiring requests.
2. **StateManager:** Maintains limiter instances using client and resource identifiers.
3. **Algorithm implementations:** Execute the configured rate-limiting strategy.

## Installation

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone <your-repository-url>
cd rate-limiter-engine
uv sync
```

## Running Tests

```bash
uv run pytest -v
```

## Technology Stack

- Python
- uv
- pytest
- threading
- collections.deque
- time.monotonic

## Project Status

Core rate-limiting algorithms, state management, and automated tests have been implemented.

## Author

**Prince Vaviya**
