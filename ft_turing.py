import json
import sys
from checkInput import checkInput


def turingMachine(config):
    (name, alphabet, blank, states,
        initial, finals, transitions) = config.values()
    print(name)


def main():
    usage = """usage: ft_turing [-h] jsonfile input

positional arguments:
    jsonfile              json description of the machine

    input                 input of the machine

optional arguments:
    -h, --help            show this help message and exit"""
    if len(sys.argv) != 3:
        print(usage)
    else:
        for arg in sys.argv:
            if arg == "-h" or arg == "--help":
                print(usage)
                break
        else:
            with open(sys.argv[1], 'r') as conf_file:
                config = json.load(conf_file)
            try:
                checkInput(config)
            except ValueError as error:
                print("Error in checkInput: {0}".format(error))
                exit
            else:
                turingMachine(config)


if __name__ == "__main__":
    main()
