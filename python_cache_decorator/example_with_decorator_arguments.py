# ─────────────────────────────────────────────
# Example: Decorator with *args and **kwargs
# (handles functions that take arguments)
# ─────────────────────────────────────────────


def logger(func):
    def wrapper(*args, **kwargs):  # accept any arguments
        print(f"▶ Calling: {func.__name__} with args={args}")
        result = func(*args, **kwargs)  # pass them to original function
        print(f"✔ Result: {result}")
        # return result

    return wrapper


def validate_input(repeat: int):
    def wrapper(func):
        def check(a, b):
            for i in range(repeat):
                print(f"▶ Calling: {func.__name__} with args={a, b}")
                if b <= 0:
                    print(f"b with this value {b} can not acceptable.")
                else:
                    print(f"The result is: {func(a, b)}")
                a *= 2
                b *= 2

        return check

    return wrapper


@validate_input(3)
def add(a, b):
    return a + b


@logger
def multiply(a, b):
    return a * b


add(3, 5)
multiply(4, 6)
# Output:
# ▶ Calling: add with args=(3, 5)
# ✔ Result: 8
# ▶ Calling: multiply with args=(4, 6)
# ✔ Result: 24
