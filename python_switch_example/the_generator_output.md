outer "for state in generate_states(3)" asks for next value
→ generate_states(3) enters the for loop, asks generate_states(2) for next value
→ generate_states(2) enters the for loop, asks generate_states(1) for next value
→ generate_states(1) enters the for loop, asks generate_states(0) for next value
→ generate_states(0) yields []
→ generate_states(1) gets [], yields [0]
→ generate_states(2) gets [0], yields [0,0]
→ generate_states(3) gets [0,0], yields [0,0,0]
→ outer loop prints {"A":0, "B":0, "C":0} ← first result printed
