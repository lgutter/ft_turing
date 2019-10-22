def transition_string(state, item):
    '''
    oneliner to print the current transition. Put in a seperate function
    because this is used in different places.
    '''
    return(
        f"({state}, '{item['read']}') -> ({item['to_state']}, '{item['write']}', {item['action']})")
