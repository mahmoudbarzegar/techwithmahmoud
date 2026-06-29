
# ─────────────────────────────────────────────
# Example 2: Solution A – Python's built-in @lru_cache
# The fastest way – just one import, one line
# ─────────────────────────────────────────────
import time
from functools import lru_cache

@lru_cache(maxsize=128)     # stores up to 128 results in memory
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print(fibonacci(35))    # 9227465
print(f"⏱ Time: {time.time() - start:.4f}s")

# Output:
# 9227465
# ⏱ Time: 0.0001s   ← thousands of times faster!