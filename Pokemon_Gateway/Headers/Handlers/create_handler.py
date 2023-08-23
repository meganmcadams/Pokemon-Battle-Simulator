import copy
import random

from ..Classes.Move import Move
from ..Classes.Pokemon import Pokemon
from ..Classes.SavedPokemon import SavedPokemon
from ..Handlers.level_handler import level_up
from ..tools import get_next_id, subheader, option, correct_type


def create(to_next_level, stored_pokemon, level, name, nickname, tid, move_levels, trainers):
    poss_keys = list(stored_pokemon.keys())
    new_mon = SavedPokemon()
    new_mon.id = get_next_id(SavedPokemon.get_all())

    dex_entry = Pokemon.get_pokemon(name)
    if dex_entry == -1:  # if could not find name in pokemon
        print("ERROR: Could not find", name, "in pokemon.")
        return
    new_mon.pid = dex_entry  # pid
    new_mon.tid = tid
    new_mon.nickname = nickname  # name
    new_mon.status = ""
    new_mon.tname = ""  # trainer name; defaulted to none
    new_mon.pname = ""  # player name; defaulted to none
    new_mon.full_name = ""  # full name

    # nickname
    if nickname.isspace():
        new_mon.nickname = "Wild " + new_mon.name

    # trainer and player
    if tid != "":
        new_mon.tname = trainers[tid]['Name']
        new_mon.plname = trainers[tid]['Player']
        new_mon.full_name = str(new_mon.tname) + "'s " + str(new_mon.name) + " (" + str(new_mon.name) + ")"
    else:
        new_mon.full_name = "Wild " + str(new_mon.name)

    # gender
    min_num = random.randrange(1, 100)
    num = float(Pokemon.get_pokemon(dex_entry).gender_ratio * 100)
    if num <= min_num:
        new_mon.gender = "Male"
    else:
        new_mon.gender = "Female"

    moves = move_levels[int(dex_entry)][0]  # set moves to list of possible moves
    if level < 3:  # if level is less than 3, have it learn 2 moves
        num = 2
    elif level < 7:
        num = 3
    else:
        num = 4
    tmp = []

    while len(tmp) < num:  # get random moves from list of options

        res_move = -1
        try:  # try to grab random from list
            res_move = random.choice(list(moves))
        except Exception:  # if only 1 in list
            res_move = moves
        tmp.append(Move.get_move(res_move))

    new_mon.moves = tmp  # store result
    new_mon.stats.hp = new_mon.base_stats.hp
    new_mon.ivs.hp = random.randrange(1, 32)
    new_mon.ivs.attack = random.randrange(1, 32)
    new_mon.ivs.defense = random.randrange(1, 32)
    new_mon.ivs.sp_attack = random.randrange(1, 32)
    new_mon.ivs.sp_defense = random.randrange(1, 32)
    new_mon.ivs.speed = random.randrange(1, 32)

    i = 0
    while i < level:
        level_up(new_mon, to_next_level, False, False)
        i += 1

    new_mon.curr_stats = copy.deepcopy(new_mon.stats)

    stored_id = new_mon['ID']

    stored_pokemon[stored_id] = new_mon
    SavedPokemon.register(new_mon)
    print("New pokemon, ", new_mon.name, ", successfully created | ID: ", stored_id, sep="")  # print success message
    return


def get_pid(pokemon, name):
    i = 0
    for key in pokemon.keys():
        try:
            if pokemon[key]['Name'] == name:
                return int(key)
        except Exception:
            pass
        i += 1

    return -1


def get_level():  # get level that user wants to make pokemon at
    subheader("Level")
    option(0, "Create random-leveled pokemon")
    option(1, "Create pokemon with level in given range")
    option(2, "Create pokemon with specified level")
    option(3, "Cancel")
    inp = input("--> ")

    try:  # try turning inp into an integer
        inp = int(inp)
    except Exception:
        inp = -1

    level = 1  # default level to 1
    if inp == 0:  # Random-leveled
        level = random.randrange(1, 99)

    elif inp == 1:
        range1 = input("From level: ")
        range2 = input("To level: ")

        try:  # try turning inputs into integers
            range1 = int(range1)
            range2 = int(range2)
        except Exception:
            print("ERROR: One or more of the inputs was not an integer")
            return -1

        if range1 < 1 or range1 >= range2 or range2 > 99:  # out of range
            print("ERROR: One or more of the inputs was out of range")
            return -1

        if inp != 3:  # if there were no errors
            level = random.randrange(range1, range2)

    elif inp == 2:
        level = input("Level: ")

        try:  # check if given level is an integer
            level = int(level)
        except Exception:
            print("ERROR:", level, "is not an integer")
            return -1

    elif inp == 3:  # Cancel
        return -1

    else:  # Out of range
        print("ERROR:", inp, "was not an option or the input wasn't an integer")
        return -1

    return level


def get_pokemon_name(pokemon):
    subheader("Pokemon Name")
    option(0, "Choose random Pokemon")
    option(1, "Choose random Pokemon by type")
    option(2, "Specify Pokemon")
    option(3, "Cancel")
    inp = input("--> ")

    try:  # check if inp is an integer
        inp = int(inp)
    except Exception:
        print("ERROR:", inp, "is not an integer")
        return -1

    if inp == 0:  # By biome
        return Pokemon.get_pokemon(random.randrange(1, Pokemon.amount - 1)).name

    elif inp == 1:  # Random Pokemon
        inp = input("Type: ")

        while True:
            mons = [i for i in Pokemon.get_all() if inp in pokemon.types]
            if len(mons) == 0:
                print("ERROR: Could not find", inp, "in types of Pokemon")
                return -1
            return random.choice(mons).name

    elif inp == 2:  # Specified name
        name = input("Name of Pokemon: ")

        pid = Pokemon.get_pokemon(name)  # try to find pokemon by name
        if pid == -1:  # if not found
            print("ERROR:", name, "not found in Pokemon")
            return -1
        else:
            return name

    elif inp == 3:  # Cancel
        return -1

    else:  # Out of range
        print("ERROR:", inp, "was not an option or the input was not an integer")
        return -1


def get_pokemon_nickname():
    subheader("Nickname")
    option(0, "No nickname")
    option(1, "Set nickname")
    inp = input("--> ")

    try:  # see if inp is an integer
        inp = int(inp)
    except Exception:
        inp = -1

    if inp == 0:
        return ""

    elif inp == 1:
        nickname = input("Nickname: ")
        return nickname

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")
        return -1


def get_pokemon_tid():
    subheader("Trainer")
    option(0, "No trainer")
    option(1, "Set trainer (ID)")
    inp = input("--> ")

    try:  # see if inp is an integer
        inp = int(inp)
    except Exception:
        inp = -1

    if inp == 0:
        return ""

    elif inp == 1:
        tid = input("Tid: ")
        return correct_type(tid)

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")
        return -1
