from Headers.Handlers.shop_handler import create_shop, delete_shop, run_shop
from Headers.save import save
from Headers.tools import header, option, correct_type


def shop_manager(shops, items, categorized_items):
    save(shops, "shops")

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
        run_shop()

    elif inp == 3:  # Exit
        return

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")

    shop_manager(shops, items, categorized_items)  # recursive call to reset menu
