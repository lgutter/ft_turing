from transition_string import transition_string


def print_status(tape, i, state, item):
    '''
    simple function to print the current status of tape, state and transition.
    it uses transition_string to get a representation of the transition.
    '''
    tape[i] = f">{tape[i]}<"
    print("".join(tape) + "  " + transition_string(state, item))
