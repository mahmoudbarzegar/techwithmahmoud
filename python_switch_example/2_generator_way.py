from collections.abc import Generator

switches = ["A", "B", "C"]


def generate_states(n: int) -> Generator[list[int], None, None]:
    if n == 0:
        yield []
    else:
        for state in generate_states(n - 1):
            yield state + [0]
            yield state + [1]


for state in generate_states(len(switches)):
    print(dict(zip(switches, state, strict=True)))
