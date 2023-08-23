from Headers import Shop
from Headers.Handlers.shop_handler import create_shop
from Headers.save import save
from Headers.tools import header, option, correct_type, print_list


def shop_manager(shops, items, categorized_items):
    save(shops, "shops.txt")

    header("Shop Manager")
    option(0, "Create Shop")
    option(1, "Delete Shop")
    option(2, "Run Shop")
    option(3, "Exit")
    inp = correct_type(input("--> "))

    if inp == 0:  # Create Shop
        create_shop()

    elif inp == 1:  # Delete Shop
        delete_shop()

    elif inp == 2:  # Run Shop
        print("Not implemented yet")

    elif inp == 3:  # Exit
        return

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")

    shop_manager(shops, items, categorized_items)  # recursive call to reset menu


def delete_shop():
    print_list(Shop.get_all())
    print("Which shop would you like to delete (-1 to cancel)?")
    to_delete = correct_type(input("--> "))
    if to_delete == -1:
        print("Action cancelled.")
    else:
        try:
            Shop.delete(to_delete)
            print(to_delete, "was successfully deleted")
        except Exception:
            print("ERROR: Could not delete", to_delete)
