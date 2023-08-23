import random

from Headers.tools import subheader, get_next_id, option, correct_type


def create_shop(shops: dict, items, categorized_items: dict) -> None:
    subheader("Create Shop")

    poss_keys = list(shops.keys())
    shop = shops[poss_keys[0]].copy()  # make a copy of existing shop

    shop['ID'] = get_next_id(shops)
    keys = ['Name', 'Location', 'Berries', 'General items', 'Machine', 'Medicine', 'Pokeballs']

    for key in keys:
        shop[key] = input(str(key) + ": ")

    print("Generate or manually input items?")
    option(0, "Generate")
    option(1, "Manually input")
    inp = correct_type(input("--> "))

    if inp == 0:  # Generate
        item_list = ""
        categories = categorized_items.keys()
        for c in categories:
            curr_items = categorized_items[c].copy()

            i = 0
            while i < int(shop[c]) and len(curr_items) > 0:  # while should get more items for that category
                random_item = random.choice(curr_items)  # get random item

                if item_list == "":  # if item list is empty so far
                    item_list = str(random_item['ID'])  # set item list to item id
                else:
                    item_list += str("," + str(random_item['ID']))  # add id to item list

                curr_items.remove(random_item)  # remove random item from curr items list of options
                i += 1  # increment

        shop['Items'] = item_list  # set items to list of generated items

    else:  # Manually input
        shop['Items'] = input("Item IDs (comma-separated): ")

    shops[int(shop['ID'])] = shop  # store shop
    print("Shop", shop['Name'], "successfully created.")  # confirmation message
