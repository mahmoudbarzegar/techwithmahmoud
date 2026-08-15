switches = ["A", "B", "C"]
results = []
switches_states = [0, 1]

for a in switches_states:
    for b in switches_states:
        for c in switches_states:
            print(dict(zip(switches, (a, b, c), strict=True)))
