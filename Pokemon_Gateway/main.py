# tools
from Headers import Move
# classes
from Headers import Pokemon
from Headers import SavedPokemon
from Headers import Trainer
from Headers.Handlers.level_handler import level_check
from Headers.Loading.load import load
# loading
from Headers.Loading.load_move_levels import load_move_levels
from Headers.Menu.battle_simulator import battle_simulator
# menu
from Headers.Menu.party_builder import party_builder
from Headers.Menu.pokemon_manager import pokemon_manager
from Headers.Menu.shop_manager import shop_manager
from Headers.Menu.trainer_manager import trainer_manager
# saving
from Headers.save import save, save_all
from Headers.tools import categorize_items, header, option

header('Pokemon Battle Simulator')

p = load("pokemon", "Resources")

# todo: move to Pokemon.get_all()


for key, value in sorted(p.items()):
    Pokemon.register(value)
moves = load("moves", "Resources")
for key, value in sorted(moves.items()):
    Move.register(value)
parties = load("parties", "Saves")
move_levels = load_move_levels(len(p))  # special load func for move_levels (move_levels[pid][level])
to_next_level = load("to_next_level", "Resources")
stored_pokemon = load("pokemon", "Saves")
for key, value in stored_pokemon.items():
    SavedPokemon.register(value)
shops = load("shops", "Saves")
t = load("trainers", "Saves")
for key,value in t.items():
    Trainer.register(value)
items = load("items", "Resources")
categorized_items = categorize_items(items)
trainers = Trainer.get_all()
for mon in SavedPokemon.iter():  # check for level ups
    level_check(mon, to_next_level, move_levels, moves)

while True:

    header("Menu")
    option(0, "Pokemon Manager")
    option(1, "Encounter Generator")
    option(2, "Trainer Manager")
    option(3, "Shop Manager")
    option(4, "Battle Simulator")
    option(5, "Party Builder")
    option(6, "Exit")
    print(SavedPokemon.get_pokemon(1).moves[0].name)
    inp = input("--> ")
    try:
        inp = int(inp)
    except Exception:
        inp = -1

    if inp == 0:  # Pokemon Manager
        pokemon_manager(stored_pokemon, to_next_level, parties, move_levels, moves, trainers)
        save(stored_pokemon, "pokemon")

    elif inp == 1:  # Encounter Generator
        print("This is not configured yet.")
        save(stored_pokemon, "pokemon")

    elif inp == 2:  # Trainer Manager
        trainer_manager()
        save(trainers, "trainers")

    elif inp == 3:  # Shop Manager
        shop_manager(shops, items, categorized_items)
        save(trainers, "trainers")
        save(shops, "shops")

    elif inp == 4:  # Battle Simulator
        battle_simulator(trainers, items, Pokemon.get_all(), stored_pokemon, parties, moves, to_next_level, move_levels)
        save(stored_pokemon, "pokemon")
        save(trainers, "trainers")

    elif inp == 5:  # Party Builder
        party_builder()
        save(parties, "parties")

    elif inp == 6:  # exit
        break

    else:
        print("ERROR:", inp, "was not an option.")

save_all()
