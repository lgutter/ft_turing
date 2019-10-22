import json
import sys
import argparse
from check_input import check_input
from print_machine import print_machine
from print_status import print_status
from transition import transition


class MachineError(Exception):
    pass


def turing_machine(config, input_):
    '''
    The actual turing machine parser. We create a loop that keeps running until
    a final state has been reached. using a for/in we find the right transition
    and let the transition function handle the transition, and print the status
    everytime we go through a transition.
    '''

    state = config['initial']
    tape = list(input_)
    i = 0
    while state not in config['finals']:
        for item in config['transitions'][state]:
            if item['read'] == tape[i]:
                (i, state) = transition(i, tape, item, config['blank'])
                print_status(tape.copy(), i, state, item)
                break
        else:
            print_status(tape.copy(), i, state, item)
            raise MachineError(
                f"No valid transition found for state '{state}' and character '{tape[i]}'")
    print("".join(tape))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', type=str,
                        help='json description of the machine')
    parser.add_argument('input', type=str,
                        help='input of the machine')

    args = parser.parse_args()
    # load the json file and print a relevant error if something goes wrong.
    try:
        with open(args.jsonfile, 'r') as conf_file:
            config = json.load(conf_file)
    except Exception as error:
        print(f"Error while loading json file: {error}")
        sys.exit(1)

    # run check_input
    try:
        check_input(config, args.input)
    except ValueError as error:
        print(f"Error in check_input: {error}")
        sys.exit(1)
    print_machine(config)
    try:
        turing_machine(config, args.input)
    except MachineError as error:
        print(f"Error in turing_machine: {error}")


if __name__ == "__main__":
    main()
