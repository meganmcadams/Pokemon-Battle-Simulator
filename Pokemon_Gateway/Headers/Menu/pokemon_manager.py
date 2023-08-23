from Headers import SavedPokemon, Party
from Headers.Handlers.battle_handler import reset_stats
from Headers.Handlers.create_handler import get_pokemon_name, get_pokemon_nickname, get_pokemon_tid, create, get_level
from Headers.save import save
from Headers.tools import header, option, print_list, correct_type


def pokemon_manager(move_levels):
    save(SavedPokemon.as_dicts(), "pokemon")

    header("Pokemon Manager")
    option(0, "Create Pokemon")
    option(1, "Delete Pokemon")
    option(2, "List Pokemon")
    option(3, "Pokemon Center")
    option(4, "Exit")
    inp = input("--> ")

    try:  # try turning inp into an integer
        inp = int(inp)
    except Exception:
        inp = -1

    if inp == 0:  # Create Pokemon
        level = get_level()

        if level != -1:
            name = get_pokemon_name()

            if name != -1:
                nickname = get_pokemon_nickname()

                if nickname != -1:
                    tid = get_pokemon_tid()

                    if tid != -1:
                        create(level, name, nickname, tid, move_levels)

    elif inp == 1:  # Delete Pokemon
        print_list(SavedPokemon.get_all())
        print("Which pokemon would you like to delete (-1 to cancel)?")
        to_delete = correct_type(input("--> "))
        if to_delete == -1:
            print("Action cancelled.")
        else:
            try:
                SavedPokemon.delete(to_delete)
                print(to_delete, "was successfully deleted")
            except Exception:
                print("ERROR: Could not delete", to_delete)

    elif inp == 2:  # List Pokemon
        print_list(SavedPokemon.get_all())

    elif inp == 3:  # Pokemon Center
        print_list(Party.get_all())
        print("Which party is going to the Pokemon Center?")
        party = input("--> ")
        try:
            pokemon_center(Party.get_party(int(party)), SavedPokemon.get_all())
        except Exception:
            print("ERROR:", party, "was not an option")

    elif inp == 4:  # Exit
        return

    else:  # Out of range
        print("ERROR:", inp, "was not an option or the input was not an integer")

    pokemon_manager(move_levels)  # recursive call to reset menu


def pokemon_center(party, stored_pokemon):  # heal all pokemon
    try:
        pokemon = party['Pokemon'].split(',')
    except Exception:
        pokemon = [party['Pokemon']]

    for p in pokemon:
        reset_stats(stored_pokemon[int(p)])
        stored_pokemon[int(p)]['Curr HP'] = stored_pokemon[int(p)]['HP']
