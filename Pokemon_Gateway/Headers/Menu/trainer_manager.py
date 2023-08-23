from Headers import Trainer
from Headers.tools import *
from .party_builder import delete_party


# TODO: all broken--funcs shouldnt have any arguments, should pull trainers from Trainer.get_all()

def trainer_manager() -> None:
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
        create_trainer()

    elif inp == 1:  # Delete Party
        delete_party()

    elif inp == 2:  # List Parties
        print_list(Trainer.get_all())

    elif inp == 3:  # Exit
        return

    else:  # incorrect input
        print("ERROR:", inp, "was not an option or the input was not an integer.")

    trainer_manager()  # recursive call to continue indefinitely until exit
    return  # return after recursive call


def create_trainer() -> None:
    name = input("Name: ")
    print("")  # print newline

    trainer = Trainer()

    trainer.id = get_next_id(Trainer.get_all())
    trainer.name = name
    Trainer.register(trainer)

    print("Trainer", trainer.id, "successfully created")


def delete_trainer() -> None:
    print_list(Trainer.get_all())
    print("Which trainer would you like to delete (-1 to cancel)?")
    to_delete = correct_type(input("--> "))
    if to_delete == -1:
        print("Action cancelled.")
    else:
        try:
            Trainer.delete(to_delete)
            print(to_delete, "was successfully deleted")
        except Exception:
            print("ERROR: Could not delete", to_delete)
