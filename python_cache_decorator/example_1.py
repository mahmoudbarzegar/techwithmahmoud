# ─────────────────────────────────────────────
# Example 1: The problem – without caching
# Same calculation runs every time, even with same input
# ─────────────────────────────────────────────

import time


def fibonacci(n):
    """Calculate nth Fibonacci number – no caching."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print(fibonacci(35))  # 9227465
print(f"⏱ Time: {time.time() - start:.4f}s")

# Output:
# 9227465
# ⏱ Time: 1.1348s   ← slow!

# Why? fibonacci(35) calls fibonacci(34) and fibonacci(33)
# fibonacci(34) ALSO calls fibonacci(33) → calculated twice!
# This repeats all the way down → millions of redundant calls
