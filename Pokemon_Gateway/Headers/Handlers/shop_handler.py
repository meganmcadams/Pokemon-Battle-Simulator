import random

from Headers import Shop, Item, Trainer
from Headers.tools import subheader, get_next_id, option, correct_type


def create_shop() -> None:
    subheader("Create Shop")
    shops = Shop.get_all()

    # reformat Shop item to be a dict as expected
    new_shop = Shop.as_dicts()[0]

    # Was too lazy to rewrite this to create a new Shop object, so I just reformat as dict and register it
    new_shop["ID"] = get_next_id(shops)
    keys = ['Name', 'Location', 'Berries', 'General items', 'Machine', 'Medicine', 'Pokeballs']

    for key in keys:
        new_shop[key] = input(str(key) + ": ")

    print("Generate or manually input items?")
    option(0, "Generate")
    option(1, "Manually input")
    inp = correct_type(input("--> "))

    categorized_items = Item.categorize()
    if inp == 0:  # Generate
        item_list = ""
        categories = categorized_items.keys()
        for c in categories:
            option(0, f"Random amount of items")
            option(1, f"Specific amount of items")
            inp = correct_type(input(f"{c} --> "))
            lower_bound = upper_bound = 0
            if inp == 0:  # Random amount of items
                lower_bound = correct_type(input("Lower bound: "))
                upper_bound = correct_type(input("Upper bound: "))
            if inp == 1:  # Specific amount of items
                upper_bount = lower_bound = correct_type(input("Amount: "))
            else:
                print("Invalid input")
                return
            if lower_bound > upper_bound or lower_bound < 0 or upper_bound < 0:
                print("Invalid input")
                return
            curr_items = categorized_items[c]
            i = 0
            item_count = random.randint(lower_bound, upper_bound)
            while i < int(item_count) and len(curr_items) > 0:  # while should get more items for that category
                random_item = random.choice(curr_items)  # get random item

                if item_list == "":  # if item list is empty so far
                    item_list = str(random_item.id)  # set item list to item id
                else:
                    item_list += f",{random_item.id}"  # add id to item list

                curr_items.remove(random_item)  # remove random item from curr items list of options
                i += 1  # increment

        new_shop['Items'] = item_list  # set items to list of generated items

    else:  # Manually input
        new_shop['Items'] = input("Item IDs (comma-separated): ")

    Shop.register(new_shop)
    print("Shop", new_shop['Name'], "successfully created.")  # confirmation message


def delete_shop():
    Shop.list_shops()
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


def run_shop():
    Shop.list_shops()
    print("Which shop would you like to run (-1 to cancel)?")
    to_run = correct_type(input("--> "))
    if to_run == -1:
        print("Action cancelled.")
    else:
        try:
            shop = Shop.get_shop(to_run)
            print("Which trainer would you like to run the shop with?")
            Trainer.list_trainers()
            trainer = correct_type(input("--> "))
            if trainer == -1:
                print("Action cancelled.")
                return
            trainer = Trainer.get_trainer(trainer)
            print(f"Now shopping with {trainer.name} (${trainer.money}) at {shop.name}")
            print("What would you like to buy?")
            dict_items = {index: item for index, item in enumerate(shop.items)}
            print(f"{'ID':<5}{'Name':<20}{'Price':<10}")
            for key, value in dict_items.items():
                print(f"{key:<5}{value.name:<20}{value.buy:<10}")
            item = correct_type(input("--> "))
            if item == -1:
                print("Action cancelled.")
                return
            item = Item.get_item(item)
            print("How many would you like to buy?")
            amount = correct_type(input("--> "))
            if amount == -1:
                print("Action cancelled.")
                return
            if amount > 0:
                if trainer.money < item.buy * amount:
                    print("You don't have enough money to buy that many.")
                    return
                print("You bought", amount, item.name + ("s" if amount > 1 else ""))
                trainer.money -= item.buy * amount
                print("You now have", trainer.money, "dollars")
                for i in range(amount):
                    trainer.items.append(item)

        except Exception as e:
            print(e)
            print("ERROR: Could not run", to_run)