def checkInput(config, input_):
    '''
    checkInput verifies if the the input is valid,
    and if the contents of the json file are what we expect.
    It verifies if every entry is of the right type, and where possible,
    it verifies that the content of fields are what we expect them to be.
    for example, it checks if everything in alphabet is a single character.
    When something is wrong, it raises a ValueError with a relevant message.
    '''

    expected = {'name': str,
                'alphabet': list,
                'blank': str,
                'states': list,
                'initial': str,
                'finals': list,
                'transitions': dict}
    if set(expected.keys()) != set(config.keys()):
        raise ValueError(f"""incorrect keys in json.
    expected: {expected.keys()}
    actual:   {config.keys()}""")

    for key in config:
        if type(config[key]) != expected[key]:
            raise ValueError(
                f"{key} should be {expected[key]} but is {type(config[key])}!")

    if config['blank'] not in config['alphabet']:
        raise ValueError("'blank' should be in 'alphabet'!")

    for key in config['alphabet']:
        if len(key) != 1:
            raise ValueError(
                f"'{key}' in 'alphabet' should be a single character!")

    if config['initial'] not in config['states']:
        raise ValueError("'initial' should be in 'states'!")

    for key in config['finals']:
        if key not in config['states']:
            raise ValueError(
                f"'{key}' in 'finals' is not in 'states'!")

    expected = {'read': config['alphabet'],
                'to_state': config['states'],
                'write': config['alphabet'],
                'action': ['LEFT', 'RIGHT']}
    for key in config['transitions'].items():
        if key[0] not in config['states']:
            raise ValueError(
                f"'{key[0]}' in 'transitions' is not in 'states'!")

        if len(key[1]) < 1:
            raise ValueError(
                f"'{key[0]}' in 'transitions' does not have any content!")

        for item in key[1]:
            if set(item.keys()) != set(expected.keys()):
                raise ValueError(
                    f"'{key[0]}' in 'transitions' has incomplete block!")

            if type(item) != dict:
                raise ValueError(
                    f"expected {dict}, found {type(item)} in '{key[0]}'!")

            for instr in item.items():
                if instr[0] not in expected:
                    raise ValueError(
                        f"'{instr[0]}' is not a valid instruction!")

                if instr[1] not in expected[instr[0]]:
                    raise ValueError(
                        f"'{instr[1]}' should be one of: {expected[instr[0]]}")

# check the input now, after we've verified the json.
    for c in input_:
        if c not in config['alphabet']:
            raise ValueError(f"'{c}' in 'input' should be in 'alphabet'")

    if config['blank'] in input_:
        raise ValueError(
            f"'blank' ('{config['blank']}') should not be in input!")
