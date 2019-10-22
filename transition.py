def transition(i, tape, item, blank):
    tape[i] = item['write']
    i = i - 1 if item['action'] == 'LEFT' else i + 1
    if i == -1:
        i += 1
        tape.insert(0, blank)
    elif i >= len(tape):
        tape.append(blank)
    return (i, item['to_state'])
