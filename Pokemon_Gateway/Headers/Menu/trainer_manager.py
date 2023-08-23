from Headers import Trainer
from Headers.tools import *
from .party_builder import delete_party


# TODO: all broken--funcs shouldnt have any arguments, should pull trainers from Trainer.get_all()

def trainer_manager(trainers: Trainer) -> None:
    print("")  # print newline
    header("Trainer Manager")
    option(0, "Create Trainer")
    option(1, "Delete Trainer")
    option(2, "List Trainers")
    option(3, "Exit")
    inp = input("--> ")
    print("")  # print newline

    try:  # try turning inp into an integer
        inp = int(inp)
    except Exception:  # if not an integer
        inp = -1  # set to -1 to classify as a wrong input

    if inp == 0:  # Create Party
        create_trainer(trainers)

    elif inp == 1:  # Delete Party
        delete_party(trainers)

    elif inp == 2:  # List Parties
        print_list(trainers)

    elif inp == 3:  # Exit
        return

    else:  # incorrect input
        print("ERROR:", inp, "was not an option or the input was not an integer.")

    trainer_manager(trainers)  # recursive call to continue indefinitely until exit
    return  # return after recursive call


def create_trainer(trainers: Trainer) -> None:
    name = input("Name: ")
    print("")  # print newline

    trainer = {}  # make dict

    for key in trainers[0].key():  # default everything to 0
        trainer[key] = 0

    trainer['ID'] = get_next_id(trainers)
    trainer['Name'] = name
    trainer['Pokedex'] = ""  # initially set to no pokedex entries
    trainer['Pokemon'] = ""  # initially set to no pokemon
    trainer['Items'] = ""  # initially set to no items
    trainers[trainer['ID']] = trainer

    print("Trainer", trainer['ID'], "successfully created")


def delete_trainer(trainers: Trainer) -> None:
    print_list(trainers)
    print("Which trainer would you like to delete (-1 to cancel)?")
    to_delete = correct_type(input("--> "))
    if to_delete == -1:
        print("Action cancelled.")
    else:
        try:
            del trainers[to_delete]
            print(to_delete, "was successfully deleted")
        except Exception:
            print("ERROR: Could not delete", to_delete)
