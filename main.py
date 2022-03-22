# tools
from Headers.tools import *

# loading
from Headers.Loading.load_pokemon import *
from Headers.Loading.load_moves import *
from Headers.Loading.load_move_levels import *
from Headers.Loading.load_to_next_level import *
from Headers.Loading.load_saves import *

# saving
from Headers.save import *

# menu
from Headers.Menu.party_builder import *
from Headers.Menu.battle_simulator import *
from Headers.Menu.pokemon_manager import *

header('Pokemon Battle Simulator')

pokemon = load_pokemon()
moves = load_moves()
parties = load_parties()
move_levels = load_move_levels(len(pokemon) - 1)
to_next_level = load_to_next_level()
stored_pokemon = load_stored_pokemon()
trainers = load_trainers()

while True:

    header("Menu")
    option(0, "Pokemon Manager")
    option(1, "Encounter Generator")
    option(2, "Trainer Manager")
    option(3, "Shop")
    option(4, "Battle Simulator")
    option(5, "Party Builder")
    option(6, "Exit")
    inp = input("--> ")

    try:
        inp = int(inp)
    except:
        inp = -1

    if inp == 0: # Pokemon Manager
        pokemon_manager(pokemon, stored_pokemon, to_next_level)
        save(stored_pokemon, "pokemon")

    elif inp == 1: # Encounter Generator
        print("test")
        save(stored_pokemon, "pokemon")

    elif inp == 2: # Trainer Manager
        print("test")
        save(trainers, "trainers")

    elif inp == 3: # Shop
        print("test")
        save(trainers, "trainers")

    elif inp == 4: # Battle Simulator
        battle_simulator(pokemon, stored_pokemon, parties)
        save(stored_pokemon, "pokemon")
        save(trainers, "trainers")

    elif inp == 5: # Party Builder
        party_builder(pokemon, stored_pokemon, parties)
        save(parties, "parties")

    elif inp == 6: # exit
        break

    else:
        print("ERROR:",inp,"was not an option.")

save_all(stored_pokemon, trainers, parties)