def save(item, filename): # save to a file
    print("Saving ",filename,"...",sep="")

    filename = "Saves/" + filename + ".txt"

    try: # try to open file
        openfile = open(filename, 'w')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    i = 0
    size = len(item[0])
    for h in item[0].keys():
        openfile.write(h)
        if i < size - 1:
            openfile.write('\t')
        i += 1
    openfile.write('\n')

    i = 0
    size = len(item)
    while i < size:
        j = len(item[i])
        k = 0
        for key in item[i].keys():
            openfile.write(str(item[i][key]))
            if k < j - 1:
                openfile.write('\t')
            k += 1
        openfile.write('\n')
        i += 1

    print("Save complete. Saved",size,"items.\n")

def save_all(stored_pokemon, trainers, parties): # save everything
    save(stored_pokemon, "pokemon")
    save(trainers, "trainers")
    save(parties, "parties")