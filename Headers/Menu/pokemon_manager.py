from Headers.tools import *
from Headers.Handlers.create_handler import *
import random
from Headers.Handlers.battle_handler import reset_stats

def pokemon_manager(pokemon, stored_pokemon, to_next_level, parties, move_levels, moves):
    header("Pokemon Manager")
    option(0, "Create Pokemon")
    option(1, "Delete Pokemon")
    option(2, "List Pokemon")
    option(3, "Pokemon Center")
    option(4, "Exit")
    inp = input("--> ")

    try: # try turning inp into an integer
        inp = int(inp)
    except:
        inp = -1

    if inp == 0: # Create Pokemon
        level = get_level()

        if level != -1:
            name = get_pokemon_name(pokemon)

            if name != -1:
                nickname = get_pokemon_nickname()
                
                if nickname != -1:
                    create(pokemon, to_next_level, stored_pokemon, level, name, nickname, move_levels, moves)

    elif inp == 1: # Delete Pokemon
        print_list(stored_pokemon)
        print("Which pokemon would you like to delete (-1 to cancel)?")
        to_delete = correct_type(input("--> "))
        if to_delete == -1:
            print("Action cancelled.")
        else:
            try:
                del stored_pokemon[to_delete]
                print(to_delete,"was successfully deleted")
            except:
                print("ERROR: Could not delete",to_delete)
        
    elif inp == 2: # List Pokemon
        print_list(stored_pokemon)

    elif inp == 3: # Pokemon Center
        print_list(parties)
        print("Which party is going to the Pokemon Center?")
        party = input("--> ")
        try:
            pokemon_center(parties[int(party)], stored_pokemon)
        except:
            print("ERROR:",party,"was not an option")

    elif inp == 4: # Exit
        return

    else: # Out of range
        print("ERROR:",inp,"was not an option or the input was not an integer")

    pokemon_manager(pokemon, stored_pokemon, to_next_level, parties, move_levels, moves) # recursive call to reset menu

def pokemon_center(party, stored_pokemon): # heal all pokemon
    try:
        pokemon = party['Pokemon'].split(',')
    except:
        pokemon = [party['Pokemon']]

    for p in pokemon:
        reset_stats(stored_pokemon[int(p)])
        stored_pokemon[int(p)]['Curr HP'] = stored_pokemon[int(p)]['HP']