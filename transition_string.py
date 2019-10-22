def transition_string(state, item):
    return(
        f"({state}, '{item['read']}') -> ({item['to_state']}, '{item['write']}', {item['action']})")
