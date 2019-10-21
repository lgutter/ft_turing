def printMachine(config):
    '''
    printMachine simply prints the machine definition from the json in a
    human readable format. For the transitions I use a for loop to print
    every transition on a seperate line with the needed information.
    '''
    print(f"""******************************************
Machine name: {config['name']}
******************************************
Alphabet: {config['alphabet']}
Blank: '{config['blank']}'
States: {config['states']}
Initial: '{config['initial']}'
Finals: {config['finals']}
******************************************
Transitions:""")
    for key in config['transitions'].items():
        for item in key[1]:
            print(
                f"({key[0]}, '{item['read']}') -> ({item['to_state']}, '{item['write']}', {item['action']})")
    print("******************************************")
