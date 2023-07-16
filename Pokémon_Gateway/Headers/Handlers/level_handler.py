from Headers.tools import *

def level_check(pokemon, p, to_next_level, move_levels, moves):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    curr_pokemon = pokemon[p['Pid']]

    if int(p['Exp']) >= int(to_next_level[int(p['Level']) + 1][curr_pokemon['Exp Growth']]): # if exp is good to level up
        level_up(curr_pokemon, p, to_next_level, move_levels, moves, True, True) # level up the pokemon
        level_check(pokemon, p, to_next_level, move_levels, moves) # recursive call in case double level up
    evolution_check(pokemon, p, to_next_level, move_levels, moves)

def level_up(pokemon, p, to_next_level, move_levels, moves, announce, sub_exp):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    #try: # ensure that pokemon is the actual pokemon itself, not the full list of all pokemon
    #    name = pokemon['Name']
    #except:
    #    pokemon = pokemon[p['Pid']]

    if sub_exp:
        p['Exp'] -= to_next_level[p['Level'] + 1][pokemon['Exp Growth']] # subtract needed exp from pokemon exp
    
    old = p.copy()

    p['Level'] += 1 # increase level
    p['HP'] = int( (int(p['HP IV']) + 2 * int(p['HP']) + (int(p['HP EV'])/4) ) * int(p['Level'])/100 ) + 10 + int(p['Level'])
    # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level

    # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
    p['HP'] = int(0.001 * (2 * pokemon['HP'] + p['HP IV'] + (0.25 * p['HP EV']) * p['Level']) + p['Level'] + 10)

    stat_list = ["Attack","Defense","Sp Attack","Sp Defense","Speed"] # make list of stats
    for s in stat_list: # set each stat
        iv = str(s) + " IV"
        ev = str(s) + " EV"
        p[s] = int(0.01 * (2 * pokemon[s] + p[iv] + (0.25 * p[ev])) * p['Level'] + 5)

    # stat info: https://pokemon.fandom.com/wiki/Statistics

    if announce is True:
        print(p['Full Name'],"leveled up to level",p['Level']) # notify user
        print_stat_changes(p, old)

    learn_moves(pokemon, p, to_next_level, moves) # learn moves if any

def print_stat_changes(new_p, old_p, stat_list = ["HP", "Attack","Defense","Sp Attack","Sp Defense","Speed"]): # make list of stats):

    for stat in stat_list:
        print(stat,": ",old_p[stat]," --> ",new_p[stat],sep="")
    print("") # print newline

def learn_moves(pokemon, p, move_levels, moves):
    try: # get moves learnable at their curr level
        learnables = move_levels[p['Pid']][p['Level']]
    except: # if there aren't any
        return

    try: # turn into a list
        curr_moves = p['Moves'].split(',')
    except: # if can't turn into a list, take the 1 move and put it in a list
        curr_moves = [p['Moves']]

    i = 0
    for m in curr_moves:
        curr_moves[i] = int(curr_moves[i])
        i += 1

    for m in learnables:
        if int(m) not in curr_moves:
            print(p['Name']," wants to learn ",moves[int(m)]['Name'],".",sep="")
            
            if len(curr_moves) >= 4:
                print("Forget a move to learn ",moves[int(m)]['Name'],"?",sep="")
                option(0, "Yes")
                option(1, "No")
                inp = input("--> ")

                try:
                    inp = int(inp)
                except:
                    print(inp,"was not an option")
                    learn_moves(pokemon, p, move_levels, moves) # try again
                    return

                if inp == 0: # Yes
                    i = 0
                    for c in curr_moves:
                        option(i, moves[int(c)]['Name'])
                        i += 1

                    inp = input("--> ")

                    try: # try to turn inp into an integer
                        inp = int(inp)
                    except:
                        print(inp,"was not an option")
                        learn_moves(pokemon, p, move_levels, moves) # try again
                        return

                    try: # try to replace move with new move
                        curr_moves[inp] = int(m)
                    except:
                        print(inp,"was not an option")
                        learn_moves(pokemon, p, move_levels, moves) # try again
                        return

                    new_moves = ""
                    i = 0
                    for c in curr_moves: # replace moves
                        new_moves += str(c)
                        if i < 3:
                            new_moves += ","
                        i += 1

                    p['Moves'] = new_moves

                    print(p['Name']," has learned ",moves[int(m)]['Name'],".",sep="")

                elif inp == 1: # No
                    pass

                else: # Incorrect input
                    print(inp,"was not an option")
                    learn_moves(pokemon, p, move_levels, moves) # try again
                    return

            else: # length of moves is less than 4
                p['Moves'] = str(p['Moves']) + "," + str(m)
                print(p['Name']," has learned ",moves[int(m)]['Name'],".",sep="")

def exp(pokemon, winning_party, defeated_party):

    print("") # print newline

    # get exp
    total = 0
    for d in defeated_party:
        total += pokemon[d['Pid']]['Exp'] * d['Level'] / 2
    total /= len(defeated_party) # get average

    for w in winning_party:
        w['Exp'] += total
        print(w['Name'],"gained",total,"experience points.")

    print("") # print newline

def evolution_check(pokemon, p, to_next_level, move_levels, moves):

    curr_pokemon = pokemon[p['Pid']]

    try:
        evolves_at_level = int(curr_pokemon['Evolves at Level'])
    except:
        return # needs a stone or can't evolve

    if p['Level'] >= evolves_at_level: # if should evolve
        print(p['Full Name']," wants to evolve.")
        option(0, "Allow")
        option(1, "Deny")
        inp = correct_type(input("--> "))

        if inp == 0:
            old_p = p.copy()
            p['Pid'] = get_pid(pokemon, curr_pokemon['Next Evo'])
            p['Pname'] = pokemon[p['Pid']]['Name']

            p['Level'] -= 1 # delevel
            level_up(old_p, p, to_next_level, move_levels, moves, False, False) # relevel

            print(p['Full Name']," evolved into ",p['Pname'],"!",sep="")

            # update full name
            if p['Tid'] == "":
                p['Full Name'] = "Wild " + str(p['Pname'])
            else:
                p['Full Name'] = str(p['Tname']) + "'s " + str(p['Pname']) + " (" + str(p['Name']) + ")"

            print_stat_changes(old_p, p)

        else:
            print(p['Full Name'],"did not evolve.")
