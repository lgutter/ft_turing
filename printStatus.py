def printStatus(tape, i):
    tape[i] = f">{tape[i]}<"
    print("".join(tape))
