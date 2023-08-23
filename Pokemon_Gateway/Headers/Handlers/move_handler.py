from Headers.tools import correct_type


def perform_move(pokemon, move, attacker, opponent, weather):
    try:  # try splitting into a list
        turns = move['Times'].split(',')
    except Exception:  # if not a list and there's only 1
        turns = [move['Times']]
    for t in turns:  # correct the type
        correct_type(t)

    # NOT DONE NOT DONE
