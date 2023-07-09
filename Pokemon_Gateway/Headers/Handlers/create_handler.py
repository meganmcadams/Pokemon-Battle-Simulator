import random
from ..Handlers.level_handler import level_up
from ..tools import get_next_id, subheader, option, correct_type


def create(pokemon, to_next_level, stored_pokemon, level, name, nickname, tid, move_levels, moves, trainers):
    poss_keys = list(stored_pokemon.keys())
    copy = stored_pokemon[poss_keys[0]].copy()  # make a copy of an existing pokemon
    for key in copy.keys():  # for key in copy
        copy[key] = int(0)  # default every value to 0

    copy['ID'] = get_next_id(stored_pokemon)  # store id

    pid = get_pid(pokemon, name)
    if pid == -1:  # if could not find name in pokemon
        print("ERROR: Could not find", name, "in pokemon.")
        return
    copy['Pid'] = pid  # pid
    copy['Pname'] = pokemon[pid]['Name']
    copy['Tid'] = tid
    copy['Name'] = nickname  # name
    copy['Status'] = ""
    copy['Tname'] = ""  # trainer name; defaulted to none
    copy['Plname'] = ""  # player name; defaulted to none
    copy['Full Name'] = ""  # full name

    # nickname
    if nickname.isspace():
        copy['Name'] = "Wild " + pokemon[pid]['Name']
    else:
        copy['Name'] = nickname

    # trainer and player
    if tid != "":
        copy['Tname'] = trainers[tid]['Name']
        copy['Plname'] = trainers[tid]['Player']
        copy['Full Name'] = str(copy['Tname']) + "'s " + str(copy['Pname']) + " (" + str(copy['Name']) + ")"
    else:
        copy['Full Name'] = "Wild " + str(copy['Pname'])

    # gender
    min_num = random.randrange(1, 100)
    num = float(pokemon[copy['Pid']]['Percent Male']) * 100
    if num <= min_num:
        copy['Gender'] = "Male"
    else:
        copy['Gender'] = "Female"

    moves = move_levels[int(pid)][0]  # set moves to list of possible moves
    res = ""
    if level < 3:  # if level is less than 3, have it learn 2 moves
        num = 2
    elif level < 7:
        num = 3
    else:
        num = 4

    i = 0
    while i < num:  # get random moves from list of options

        res_move = -1
        try:  # try to grab random from list
            res_move = str(random.choice(list(moves)))
        except Exception:  # if only 1 in list
            res_move = str(moves)

        if res_move not in res:  # if haven't stored it already
            res += res_move
            if i < num - 1:
                res += ","
        i += 1

    copy['Moves'] = res  # store result
    copy['HP'] = pokemon[pid]['HP']
    copy['HP IV'] = random.randrange(1, 32)
    copy['Attack IV'] = random.randrange(1, 32)
    copy['Defense IV'] = random.randrange(1, 32)
    copy['Sp Attack IV'] = random.randrange(1, 32)
    copy['Sp Defense IV'] = random.randrange(1, 32)
    copy['Speed IV'] = random.randrange(1, 32)

    i = 0
    while i < level:
        level_up(pokemon[pid], copy, to_next_level, move_levels, moves, False, False)
        i += 1

    copy['Curr HP'] = copy['HP']
    copy['Curr Attack'] = copy['Attack']
    copy['Curr Defense'] = copy['Defense']
    copy['Curr Sp Attack'] = copy['Sp Attack']
    copy['Curr Sp Defense'] = copy['Sp Defense']
    copy['Curr Speed'] = copy['Speed']

    stored_id = copy['ID']

    stored_pokemon[stored_id] = copy.copy()

    print("New pokemon, ", copy['Pname'], ", successfully created | ID: ", stored_id, sep="")  # print success message
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
        return pokemon[random.randrange(1, len(pokemon) - 1)]['Name']

    elif inp == 1:  # Random Pokemon
        inp = input("Type: ")

        count = 0
        while True:
            i = random.randrange(0, len(pokemon) - 1)
            if pokemon[i]['Type1'] == inp or pokemon[i]['Type2'] == inp:
                return pokemon[i]['Name']
            else:
                count += 1
                if i > len(pokemon) - 1:  # if at end
                    i = 0
                else:  # if not at end
                    i += 1
            if count >= len(pokemon) / 10:  # if have gone through 10% of the pokemon and not found one yet
                print("ERROR: Could not find", inp, "in types of Pokemon")
                return -1

    elif inp == 2:  # Specified name
        name = input("Name of Pokemon: ")

        pid = get_pid(pokemon, name)  # try to find pokemon by name
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
