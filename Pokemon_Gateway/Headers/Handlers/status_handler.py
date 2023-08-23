import random

from Headers import SavedPokemon, Move


def status_damage(curr_pokemon: SavedPokemon):  # handle status effects at end of cycle

    if curr_pokemon.status != "":  # if has a status, handle status effects
        if curr_pokemon.status == "Burn" or curr_pokemon.status == "Poison":
            print(curr_pokemon.name, "was hurt by its", curr_pokemon.status)
            curr_pokemon.curr_stats.hp -= (int(curr_pokemon.stats.hp) * 0.05)  # decrease health by 5%
            print(curr_pokemon.curr_stats.hp)
    return


def status_check(move: Move, opponent: SavedPokemon):
    # todo: update statuses to use yeet rates and affliction rates--make a json file for this
    add_status = True
    if move.status == "":
        add_status = False
    elif opponent.status != "":
        num = random.randrange(1, 4)  # 25% chance of yeeting the status
        if num == 1:  # yeet the status
            print(opponent.name, "is no longer afflicted with", opponent.status)
            opponent.status = ""

    if add_status:  # if can add a status
        try:  # try splitting possible statuses into a list
            statuses = move.status.split(',')
        except Exception:  # if only one in list
            statuses = [move.status]

        i = random.randrange(0, len(statuses))  # pick random status from list
        min_num = random.randrange(1, 100)
        num = float(move['Status Chance']) * 100  # get chance of status effect

        if num >= min_num:
            print(opponent.name, "was afflicted with", statuses[i])
            opponent.status = statuses[i]
            return
        else:
            return
