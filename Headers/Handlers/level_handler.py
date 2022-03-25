from Headers.tools import *

def level_check(pokemon, p, to_next_level, move_levels, moves):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    pokemon['Exp'] = int(pokemon['Exp'])
    pokemon['Level'] = int(pokemon['Level'])
    p['Exp Growth'] = int(p['Exp Growth'])

    if int(pokemon['Exp']) >= int(to_next_level[int(pokemon['Level']) + 1][int(p['Exp Growth'])]): # if exp is good to level up
        level_up(pokemon, p, to_next_level, move_levels, moves, True, True) # level up the pokemon
        level_check(pokemon, p, move_levels, to_next_level) # recursive call in case double level up

def level_up(pokemon, p, to_next_level, move_levels, moves, announce, sub_exp):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    if sub_exp:
        pokemon['Exp'] -= to_next_level[pokemon['Level'] + 1][p['Exp Growth']] # subtract needed exp from pokemon exp
    
    old = pokemon.copy()

    pokemon['Level'] += 1 # increase level
    pokemon['HP'] = int( (int(pokemon['HP IV']) + 2 * int(p['HP']) + (int(pokemon['HP EV'])/4) ) * int(pokemon['Level'])/100 ) + 10 + int(pokemon['Level'])
    # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level

    # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
    pokemon['Attack'] = int((int(p['Attack']) * 2 + int(pokemon['Attack IV']) + int(pokemon['Attack EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['Defense'] = int((int(p['Defense']) * 2 + int(pokemon['Defense IV']) + int(pokemon['Defense EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['Sp Attack'] = int((int(p['Sp Attack']) * 2 + int(pokemon['Sp Attack IV']) + int(pokemon['Sp Attack EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['Sp Defense'] = int((int(p['Sp Defense']) * 2 + int(pokemon['Sp Defense IV']) + int(pokemon['Sp Defense EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['Speed'] = int((int(p['Speed']) * 2 + int(pokemon['Speed IV']) + int(pokemon['Speed EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    # stat guide: https://gamefaqs.gamespot.com/boards/989552-pokemon-black-version/58673641

    if announce is True:

        print(pokemon['Name'],"leveled up to level",pokemon['Level']) # notify user
        print("Level:",old['Level'],"-->",pokemon['Level'])
        print("HP:",old['HP'],"-->",pokemon['HP'])
        print("Attack:",old['Attack'],"-->",pokemon['Attack'])
        print("Defense:",old['Defense'],"-->",pokemon['Defense'])
        print("Sp Attack:",old['Sp Attack'],"-->",pokemon['Sp Attack'])
        print("Sp Defense:",old['Sp Defense'],"-->",pokemon['Sp Defense'])
        print("Speed:",old['Speed'],"-->",pokemon['Speed'],"\n")

    learn_moves(pokemon, p, to_next_level, moves) # learn moves if any

def learn_moves(pokemon, p, move_levels, moves):
    try:
        learnables = move_levels[int(p['Pid'])][int(p['Level'])]
    except:
        return

    try:
        curr_moves = p['Moves'].split(',')
    except:
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