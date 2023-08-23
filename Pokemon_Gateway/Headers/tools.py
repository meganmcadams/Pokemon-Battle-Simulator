import typing


def header(text: str) -> None:
    text_size = len(text)
    print("")  # print newline

    if text_size >= 70:
        print(text)
    else:

        header_size = (70 - text_size) / 2

        i = 0
        while i < header_size:  # print left lines
            print('-', end='')
            i += 1

        print(text, end='')  # print header

        i = 0
        while i < header_size:  # print right lines
            print('-', end='')
            i += 1

        print('')  # newline


def subheader(text: str) -> None:
    text_size = len(text)
    print("")  # print newline
    if text_size >= 20:
        print("-" + text)
    else:

        header_size = (15 - text_size)

        i = 0
        while i < header_size:  # print left lines
            print('-', end='')
            i += 1

        print(text)  # print subheader


def option(num: int, text: str) -> None:
    print(f"    | {num}: {text}")


def print_list(items: dict) -> None:
    if len(items) < 1:  # if there aren't any items to print
        print("ERROR: There are", len(items), "items.")
        return

    for item_key in items.keys():  # for every item
        for key in items[item_key]:  # for col in item
            print(key, ": ", items[item_key][key], sep="")  # print key's contents
        print("")  # print newline


def get_next_id(dict_: dict) -> int:
    keylist = sorted(list(dict_.keys()))

    prev = -1
    for key in keylist:
        if key != prev + 1:
            return prev + 1
        prev += 1

    return len(keylist)


def correct_type(item: typing.Any) -> typing.Union[float, int, str]:  # fix the type, if possible
    try:
        item = int(item)
    except Exception:
        try:
            item = float(item)
        except Exception:
            item = str(item)

    return item


def get_pid(pokemon, name):
    i = 0
    for key in pokemon.keys():
        try:
            if pokemon[key]['Name'] == name:
                return int(key)
        except Exception:
            pass
        i += 1

    return -1


def categorize_items(items: dict) -> dict:
    categories = []
    items_categorized = {}
    for key in items.keys():  # for every item
        item = items[key]
        category = str(item['Type'])

        if category not in categories:  # if category not already stored as a key
            items_categorized[category] = []  # make list for that category
            categories.append(category)  # signal that we've made a list for this category already

        items_categorized[category].append(item)  # add item to appropriate category

    return items_categorized
