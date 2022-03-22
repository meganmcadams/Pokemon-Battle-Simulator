from Headers.tools import *
from Headers.create_handler import *

def pokemon_manager(pokemon, stored_pokemon, to_next_level):
    header("Pokemon Manager")
    option(0, "Create Pokemon")
    option(1, "Delete Pokemon")
    option(2, "List Pokemon")
    inp = input("--> ")

    try: # try turning inp into an integer
        inp = int(inp)
    except:
        inp = -1

    if inp == 0:
        print("test")