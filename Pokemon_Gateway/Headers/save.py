import os.path


def save(items, filename):  # save to a file
    print("Saving ", filename, "...", sep="")

    filename = os.path.join("Saves", filename + ".txt")

    try:  # try to open file
        openfile = open(filename, 'w')
    except:  # if couldn't open it
        print("ERROR: Could not open", filename)
        exit()

    rows = len(items)
    if rows < 1:
        print("ERROR: There are 0 items.")
        return

    # headers
    poss_keys = list(items.keys())
    cols = len(items[poss_keys[0]])
    i = 0
    for key in items[poss_keys[0]].keys():
        if i == cols - 1:
            openfile.write(str(key))
            openfile.write('\n')
        else:
            openfile.write(str(key))
            openfile.write('\t')
        i += 1

    cols = len(items[poss_keys[0]])
    for item_key in items.keys():
        i = 0
        for key in items[item_key].keys():
            if i == cols - 1:
                openfile.write(str(items[item_key][key]))
                openfile.write("\n")
            else:
                openfile.write(str(items[item_key][key]))
                openfile.write("\t")
            i += 1

    openfile.close()

    print("Save complete. Saved", len(items), "items.\n")


def save_all(stored_pokemon, trainers, parties, shops):  # save everything
    save(stored_pokemon, "pokemon")
    save(trainers, "trainers")
    save(parties, "parties")
    save(shops, "shops")
