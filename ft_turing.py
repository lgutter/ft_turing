import json
import sys
import argparse
from checkInput import checkInput
from printMachine import printMachine
from printStatus import printStatus


class MachineError(Exception):
    pass


def turingMachine(config, input_):
    state = config['initial']
    tape = list(input_)
    transitions = config['transitions']
    i = 0
    while state not in config['finals']:
        for item in transitions[state]:
            if item['read'] == tape[i]:
                printStatus(tape, i)
                tape[i] = item['write']
                state = item['to_state']
                i = i - 1 if item['action'] == 'LEFT' else i + 1
                break
        else:
            raise MachineError(
                f"No valid transition found for state '{state}' and character '{item['read']}'")
    printStatus(tape, i)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', type=str,
                        help='json description of the machine')
    parser.add_argument('input', type=str,
                        help='input of the machine')

    args = parser.parse_args()
    try:
        with open(args.jsonfile, 'r') as conf_file:
            config = json.load(conf_file)
    except ValueError as error:
        print(f"Error while loading json file: {error}")
        return

    try:
        checkInput(config, args.input)
    except ValueError as error:
        print(f"Error in checkInput: {error}")
        return
    printMachine(config)
    try:
        turingMachine(config, args.input)
    except MachineError as error:
        print(f"Error in turingMachine: {error}")


if __name__ == "__main__":
    main()
