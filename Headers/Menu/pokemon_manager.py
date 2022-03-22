from Headers.tools import *
from Headers.Handlers.create_handler import *
import random

def pokemon_manager(pokemon, stored_pokemon, to_next_level):
    header("Pokemon Manager")
    option(0, "Create Pokemon")
    option(1, "Delete Pokemon")
    option(2, "List Pokemon")
    option(3, "Exit")
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
                    create(pokemon, to_next_level, stored_pokemon, level, name, nickname)

    elif inp == 1: # Delete Pokemon
        print("Not configured")
        
    elif inp == 2: # List Pokemon
        print_list(stored_pokemon)

    elif inp == 3: # Exit
        return

    else: # Out of range
        print("ERROR:",inp,"was not an option or the input was not an integer")

    pokemon_manager(pokemon, stored_pokemon, to_next_level) # recursive call to reset menu