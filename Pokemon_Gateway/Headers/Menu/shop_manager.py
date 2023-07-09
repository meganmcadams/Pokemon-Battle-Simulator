from ..save import save
from ..tools import header, option, correct_type
from ..Handlers.shop_handler import create_shop


def shop_manager(shops, items, categorized_items):
    save(shops, "shops.txt")

    header("Shop Manager")
    option(0, "Create Shop")
    option(1, "Delete Shop")
    option(2, "Run Shop")
    option(3, "Exit")
    inp = correct_type(input("--> "))

    if inp == 0:  # Create Shop
        create_shop(shops, items, categorized_items)

    elif inp == 1:  # Delete Shop
        pass
    elif inp == 2:  # Run Shop
        pass

    elif inp == 3:  # Exit
        return

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")

    shop_manager(shops, items, categorized_items)  # recursive call to reset menu
