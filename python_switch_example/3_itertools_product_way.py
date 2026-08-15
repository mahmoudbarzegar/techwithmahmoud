from itertools import product

switches = ["A", "B", "C"]
switches_states = [0, 1]

for state in product(switches_states, repeat=len(switches)):
    print(dict(zip(switches, state, strict=True)))
