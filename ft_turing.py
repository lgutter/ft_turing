import json
import sys
import argparse
from checkInput import checkInput


def turingMachine(config, input):
    (name, alphabet, blank, states,
        initial, finals, transitions) = config.values()
    print(name)


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
        print("Error while loading json file: {0}".format(error))
        sys.exit(1)

    try:
        checkInput(config, args.input)
    except ValueError as error:
        print("Error in checkInput: {0}".format(error))
        exit
    else:
        turingMachine(config, args.input)


if __name__ == "__main__":
    main()
