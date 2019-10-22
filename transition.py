def transition(i, tape, item, blank):
    '''
    Transition handles all the steps in transitioning from a state to the next
    state. it writes the correct character, updates the index, extends the tape
    if needed, and returns the new index + new state.
    '''
    tape[i] = item['write']
    i = i - 1 if item['action'] == 'LEFT' else i + 1
    if i == -1:
        i += 1
        tape.insert(0, blank)
    elif i >= len(tape):
        tape.append(blank)
    return (i, item['to_state'])
