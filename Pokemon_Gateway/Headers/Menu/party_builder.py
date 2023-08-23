from Headers.Classes.Party import Party
from Headers.Classes.SavedPokemon import SavedPokemon
from Headers.tools import *


def party_builder():
    print("")  # print newline
    header("Party Builder")
    option(0, "Create Party")
    option(1, "Delete Party")
    option(2, "List Parties")
    option(3, "Exit")
    inp = input("--> ")
    print("")  # print newline

    try:  # try turning inp into an integer
        inp = int(inp)
    except Exception:  # if not an integer
        inp = -1  # set to -1 to classify as a wrong input

    if inp == 0:  # Create Party
        create_party()

    elif inp == 1:  # Delete Party
        delete_party()

    elif inp == 2:  # List Parties
        print_list(Party.get_all())

    elif inp == 3:  # Exit
        return

    else:  # incorrect input
        print("ERROR:", inp, "was not an option or the input was not an integer.")

    party_builder()  # recursive call to continue indefinitely until exit
    return  # return after recursive call


def create_party():
    name = input("Name: ")
    pokemon = input("Pokemon (comma-separated): ")
    print("")  # print newline

    pokemon_split = pokemon.split(',')  # split pokemon by commas for error checking

    for p in pokemon_split:
        try:  # try turning to int
            SavedPokemon.get_pokemon(correct_type(p))
        except Exception:
            print("ERROR:", p, "is not an integer or is not a stored pokemon")
            return
    id_ = get_next_id(Party.get_all())
    party = Party(id_, name, [SavedPokemon.get_pokemon(int(p)) for p in pokemon_split])
    Party.register(id_, party)

    print("Party", party.id, "successfully created")


def delete_party():
    print_list(Party.get_all())
    print("Which party would you like to delete (-1 to cancel)?")
    to_delete = correct_type(input("--> "))
    if to_delete == -1:
        print("Action cancelled.")
    else:
        try:
            Party.delete(to_delete)
            print(to_delete, "was successfully deleted")
        except Exception:
            print("ERROR: Could not delete", to_delete)
