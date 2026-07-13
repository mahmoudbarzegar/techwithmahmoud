# ─────────────────────────────────────────────
# Example 3: Build your own @cache from scratch
# So you understand exactly what lru_cache does internally
# ─────────────────────────────────────────────
import time
from functools import wraps


def cache(func):
    """Stores results of previous calls in a dictionary.

    If the same arguments are passed again → return stored result instantly.
    """
    stored_results = {}  # { arguments : result }

    @wraps(func)
    def wrapper(*args):
        if args in stored_results:
            print(f"   [cache hit]  {func.__name__}{args}")
            return stored_results[args]  # return instantly, no recalculation

        print(f"   [cache miss] {func.__name__}{args} → calculating...")
        result = func(*args)  # calculate for the first time
        stored_results[args] = result  # save for next time
        return result

    wrapper.cache_info = stored_results  # type: ignore # expose cache for inspection
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print("\n── First call: fibonacci(6) ──")
print(f"Result: {fibonacci(6)}\n")
print(f"⏱ Time: {time.time() - start:.4f}s\n")

# print(fibonacci.cache_info)


# Output:
# [cache miss] fibonacci(0) → calculating...
# [cache miss] fibonacci(1) → calculating...
# [cache miss] fibonacci(2) → calculating...
# [cache miss] fibonacci(3) → calculating...
# [cache miss] fibonacci(4) → calculating...
# [cache miss] fibonacci(5) → calculating...
# [cache miss] fibonacci(6) → calculating...
# Result: 8

start = time.time()
print("── Second call: fibonacci(4) ──")
print(f"Result: {fibonacci(4)}\n")
print(f"⏱ Second call time: {time.time() - start:.4f}s\n")

# Output:
# [cache hit]  fibonacci(4)
# Result:     ← instant! no recalculation at all
