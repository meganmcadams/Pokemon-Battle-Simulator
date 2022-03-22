import random
from Headers.level_handler import *

def create(pokemon, to_next_level, stored_pokemon, level, name):
    copy = stored_pokemon[0].copy() # make a copy of the first stored pokemon
    for key in copy.keys(): # for key in copy
        copy[key] = int(0) # default every value to 0

    copy['ID'] = len(stored_pokemon) # store id

    pid = get_pid(pokemon, name)
    if pid == -1: # if could not find name in pokemon
        print("ERROR: Could not find",name,"in pokemon.")
        exit()
    copy['Pid'] = pid # pid
    copy['Tid'] = -1 # tid
    copy['Name'] = -1 # name
    copy['Status'] = ""
    
    moves = pokemon[pid]['Learnable Moves'].split(',') # set moves to list of possible moves
    res = ""
    if level < 3:
        num = 2
    elif level < 7:
        num = 3
    else:
        num = 4

    i = 0
    while i < num: # get random moves from list of options
        res += str(random.choice(moves))
        if i < num - 1:
            res += ","
        i += 1

    copy['Moves'] = res # store result
    copy['HP IV'] = random.randrange(1,32)
    copy['Defense IV'] = random.randrange(1,32)
    copy['SP Attack IV'] = random.randrange(1,32)
    copy['SP Defense IV'] = random.randrange(1,32)
    copy['Speed IV'] = random.randrange(1,32)
    
    i = 0
    while i < level:
        level_up(copy, pokemon[pid], to_next_level, False, False)
        i += 1

    copy['Curr HP'] = copy['HP']

    stored_pokemon.append(copy)

def get_pid(pokemon, name):

    i = 0
    for p in pokemon:
        try:
            if p['Name'] == name:
                return i
        except:
            pass
        i += 1

    return -1