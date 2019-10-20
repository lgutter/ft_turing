def checkInput(config):
    expected = {'name': str,
                'alphabet': list,
                'blank': str,
                'states': list,
                'initial': str,
                'finals': list,
                'transitions': dict}
    if set(expected.keys()) != set(config.keys()):
        raise ValueError("incorrect keys in json")
    for key in config:
        if type(config[key]) != expected[key]:
            raise ValueError("{0} should be {1}, but is {2}!"
                             .format(key, expected[key], type(config[key])))
    if config['blank'] not in config['alphabet']:
        raise ValueError("'blank' should be in 'alphabet'!")
    for key in config['alphabet']:
        if len(key) != 1:
            raise ValueError("'" + key + "'" +
                             " in 'alphabet' should be a single character!")
    if config['initial'] not in config['states']:
        raise ValueError("'initial' should be in 'states'!")
    for key in config['finals']:
        if key not in config['states']:
            raise ValueError(key + "in 'finals' is not in 'states'!")
    expected = {'read': config['alphabet'],
                'to_state': config['states'],
                'write': config['alphabet'],
                'action': ['LEFT', 'RIGHT']}
    for key in config['transitions'].items():
        if key[0] not in config['states']:
            raise ValueError(key[0] + " in 'transitions' is not in 'states'!")
        if len(key[1]) < 1:
            raise ValueError(key[0] + " does not have any instructions!")
        for item in key[1]:
            if type(item) != dict:
                raise ValueError("expected {0}, found {1} in '{2}'!"
                                 .format(dict, type(item), key[0]))
            for instr in item.items():
                if instr[0] not in expected:
                    raise ValueError(instr[0] + "is not a valid instruction!")
                if instr[1] not in expected[instr[0]]:
                    raise ValueError("'{0}' should be one of the following:{1}"
                                     .format(instr[1], expected[instr[0]]))
