import random

from Headers import Shop, Item
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
            # todo: figure out how this works
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
