from transition_string import transition_string


def print_status(tape, i, state, item):
    tape[i] = f">{tape[i]}<"
    print("".join(tape) + "  " + transition_string(state, item))
