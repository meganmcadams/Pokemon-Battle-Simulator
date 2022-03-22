def level_check(pokemon, p, to_next_level):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    if pokemon['Exp'] >= to_next_level[pokemon['Level'] + 1][p['Exp Growth']]: # if exp is good to level up
        level_up(pokemon, p, to_next_level, True, True) # level up the pokemon
        level_check(pokemon, p, to_next_level) # recursive call in case double level up

def level_up(pokemon, p, to_next_level, announce, sub_exp):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    if sub_exp:
        pokemon['Exp'] -= to_next_level[pokemon['Level'] + 1][p['Exp Growth']] # subtract needed exp from pokemon exp
    
    old = pokemon.copy()

    pokemon['Level'] += 1 # increase level
    pokemon['HP'] = int( (int(pokemon['HP IV']) + 2 * int(p['HP']) + (int(pokemon['HP EV'])/4) ) * int(pokemon['Level'])/100 ) + 10 + int(pokemon['Level'])
    # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level

    # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
    pokemon['Defense'] = int((int(p['Defense']) * 2 + int(pokemon['Defense IV']) + int(pokemon['Defense EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['SP Attack'] = int((int(p['SP Attack']) * 2 + int(pokemon['SP Attack IV']) + int(pokemon['SP Attack EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['SP Defense'] = int((int(p['SP Defense']) * 2 + int(pokemon['SP Defense IV']) + int(pokemon['SP Defense EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    pokemon['Speed'] = int((int(p['Speed']) * 2 + int(pokemon['Speed IV']) + int(pokemon['Speed EV'])/4) * int(pokemon['Level']) / 100) + 10 + int(pokemon['Level'])
    # stat guide; https://gamefaqs.gamespot.com/boards/989552-pokemon-black-version/58673641

    if announce is True:

        print(pokemon['Name'],"leveled up to level",pokemon['Level']) # notify user
        print("Level:",old['Level'],"-->",pokemon['Level'])
        print("HP:",old['HP'],"-->",pokemon['HP'])
        print("Defense:",old['Defense'],"-->",pokemon['Defense'])
        print("SP Attack:",old['SP Attack'],"-->",pokemon['SP Attack'])
        print("SP Defense:",old['SP Defense'],"-->",pokemon['SP Defense'])
        print("Speed:",old['Speed'],"-->",pokemon['Speed'],"\n")