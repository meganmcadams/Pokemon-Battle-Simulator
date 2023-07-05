# tools
from Headers.tools import categorize_items, header, option
from Headers.Handlers.level_handler import level_check

# classes
from Headers.Classes.Pokemon import Pokemon
from Headers.Classes.Trainers import Trainers

# loading
from Headers.Loading.load_move_levels import load_move_levels
from Headers.Loading.load import load

# saving
from Headers.save import save, save_all

# menu
from Headers.Menu.party_builder import party_builder
from Headers.Menu.battle_simulator import battle_simulator
from Headers.Menu.pokemon_manager import pokemon_manager
from Headers.Menu.trainer_manager import trainer_manager
from Headers.Menu.shop_manager import shop_manager

header('Pokemon Battle Simulator')

p = load("pokemon", "Resources")
pokemon = Pokemon(p) # store in class
moves = load("moves", "Resources")
parties = load("parties", "Saves")
move_levels = load_move_levels(len(pokemon.list)) # special load func for move_levels (move_levels[pid][level])
to_next_level = load("to_next_level","Resources")
stored_pokemon = load("pokemon","Saves")
shops = load("shops","Saves")
t = load("trainers","Saves")
trainers = Trainers(t) # store in class
items = load("items","Resources")
categorized_items = categorize_items(items)

for key in stored_pokemon: # check for level ups
    level_check(pokemon.list, stored_pokemon[key], to_next_level, move_levels, moves)

while True:

    header("Menu")
    option(0, "Pokemon Manager")
    option(1, "Encounter Generator")
    option(2, "Trainer Manager")
    option(3, "Shop Manager")
    option(4, "Battle Simulator")
    option(5, "Party Builder")
    option(6, "Exit")
    inp = input("--> ")

    try:
        inp = int(inp)
    except:
        inp = -1

    if inp == 0: # Pokemon Manager
        pokemon_manager(pokemon.list, stored_pokemon, to_next_level, parties, move_levels, moves, trainers.list)
        save(stored_pokemon, "pokemon")

    elif inp == 1: # Encounter Generator
        print("This is not configured yet.")
        save(stored_pokemon, "pokemon")

    elif inp == 2: # Trainer Manager
        trainer_manager(trainers)
        save(trainers.list, "trainers")

    elif inp == 3: # Shop Manager
        shop_manager(shops, items, categorized_items)
        save(trainers.list, "trainers")
        save(shops, "shops")

    elif inp == 4: # Battle Simulator
        battle_simulator(trainers, items, pokemon.list, stored_pokemon, parties, moves, to_next_level, move_levels)
        save(stored_pokemon, "pokemon")
        save(trainers.list, "trainers")

    elif inp == 5: # Party Builder
        party_builder(pokemon.list, stored_pokemon, parties)
        save(parties, "parties")

    elif inp == 6: # exit
        break

    else:
        print("ERROR:",inp,"was not an option.")

save_all(stored_pokemon, trainers.list, parties, shops)