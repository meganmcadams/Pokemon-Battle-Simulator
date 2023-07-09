from ..tools import *
import random


def get_move(pokemon, moves):
    subheader("Move")

    try:  # try breaking into list
        pokemon_moves = pokemon['Moves'].split(',')
    except:  # if only 1 pokemon
        pokemon_moves = [pokemon['Moves']]

    i = 0
    for m in pokemon_moves:  # set pokemon_moves[i] to actual move info, not just mid
        try:  # try to find move info
            pokemon_moves[i] = moves[int(pokemon_moves[i])]
        except:
            print("ERROR: Could not find", pokemon_moves[i], "in moves")
            return -3  # error

        i += 1

    options = [-2, -1]
    option(-2, "Pass")
    option(-1, "Throw Pokeball")

    i = 0
    for m in pokemon_moves:  # print move options
        option(i, str(str(m['Name']) + " (" + str(m['Description']) + ")"))
        options.append(i)
        i += 1

    inp = input("--> ")

    try:  # try turning to integer
        inp = int(inp)
    except:
        print("ERROR:", inp, "was not an option")
        return -3  # error

    if inp not in options:
        print("ERROR:", inp, "was not an option")
        return -3  # error

    if inp == -1 or inp == -2:  # if pass or throw pokeball
        return inp
    return pokemon_moves[inp]  # else return move


def accuracy_check(curr_pokemon, move):  # determine if a move hits or misses
    if int(curr_pokemon['Flinched']) == 1:  # flinch check
        curr_pokemon['Flinched'] = 0
        print(curr_pokemon['Name'], "flinched!")
        return False

    if curr_pokemon['Status'] == "Sleep" or curr_pokemon['Status'] == "Freeze":
        print(curr_pokemon['Name'], "is afflicted by", curr_pokemon['Status'])
        return False

    if curr_pokemon['Status'] == "Confusion":
        num = random.randrange(1, 2)  # 50% chance to be hurt by confusion
        if num == 1:
            print(curr_pokemon['Name'], "was hurt by its confusion!")
            curr_pokemon['Curr HP'] -= (int(curr_pokemon['HP']) * 0.05)  # decrease health by 5%
            return False
        else:
            print(curr_pokemon['Name'], "pushed through its confusion.")

    if curr_pokemon['Status'] == "Paralysis":
        num = random.randrange(1, 2)  # 50% to be paralyzed
        if num == 1:
            print(curr_pokemon['Name'], "is paralyzed!")
            return False

    # if passed the status check, check if the move misses or not
    min_num = random.randrange(1, 100)
    num = float(move['Accuracy']) * 100

    if num >= min_num:
        return True
    else:
        print(str(move['Name'] + " missed!"))
        return False


def stat_change_check(move, attacker, opponent):
    # opponent stat changes
    opponent['Curr Speed'] += int(move['O Speed'])
    opponent['Curr Attack'] += int(move['O Attack'])
    opponent['Curr Defense'] += int(move['O Defense'])
    opponent['Curr Sp Attack'] += int(move['O Sp Attack'])
    opponent['Curr Sp Defense'] += int(move['O Sp Defense'])

    # attacker stat changes
    attacker['Curr Speed'] += int(move['O Speed'])
    attacker['Curr Attack'] += int(move['O Attack'])
    attacker['Curr Defense'] += int(move['O Defense'])
    attacker['Curr Sp Attack'] += int(move['O Sp Attack'])
    attacker['Curr Sp Defense'] += int(move['O Sp Defense'])

    # flinch check
    if int(move['Flinch']) > 0:
        num = random.randrange(1, 2)
        if num == 1:
            opponent['Flinched'] = 1  # set flinched to true


def get_target(pokemon, stored_pokemon, current_party, opposing_party):
    subheader("Target")

    try:  # try breaking into list
        opposing_party = opposing_party['Pokemon'].split(',')
    except:  # if only 1 pokemon
        opposing_party = [opposing_party['Pokemon']]

    i = 0
    for p in opposing_party:  # set opposing_party[i] to actual info
        try:
            opposing_party[i] = stored_pokemon[int(opposing_party[i])]
        except:
            print("ERROR: Could not find", opposing_party[i], "in pokemon")
            return -1

        i += 1

    options = []
    i = 0
    for p in opposing_party:  # print target options
        if p['Curr HP'] <= 0:  # if the pokemon is dead
            pass
        else:
            option(i, str(str(pokemon[int(p['Pid'])]['Name']) + " (" + str(p['ID']) + ")" + " | Curr HP: " + str(
                p['Curr HP']) + "/" + str(p['HP'])))
            options.append(i)
        i += 1

    inp = correct_type(input("--> "))

    if inp not in options:
        print("ERROR:", inp, "was not an option")
        return -1

    return opposing_party[inp]


def weather_check(move, weather):
    if move['Weather'] != "":
        weather = move['Weather']


def reset_stats(pokemon):
    pokemon['Curr Attack'] = int(pokemon['Attack'])
    pokemon['Curr Defense'] = int(pokemon['Defense'])
    pokemon['Curr Sp Attack'] = int(pokemon['Sp Attack'])
    pokemon['Curr Sp Defense'] = int(pokemon['Sp Defense'])
    pokemon['Curr Speed'] = int(pokemon['Speed'])


def health_check(party_order, party1_pokemon, party2_pokemon, party_order_names, fainted_pokemon):  #
    for p in party_order:
        if int(p['Curr HP']) <= 0 and p not in fainted_pokemon:
            print(party_order_names[p['ID']], "has fainted!")
            fainted_pokemon.append(p)  # add to list of fainted pokemon

    party1_count = 0
    for p in party1_pokemon:
        if int(p['Curr HP']) > 0:
            party1_count += 1

    party2_count = 0
    for p in party2_pokemon:
        if int(p['Curr HP']) > 0:
            party2_count += 1

    if party1_count < 1:
        return 2  # 2 won

    if party2_count < 1:
        return 1  # 1 won

    return 0
