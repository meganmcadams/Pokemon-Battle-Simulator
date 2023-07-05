import re


def load_pokemon():
    print("Loading pokemon...")

    filename = "Resources/pokemon.txt"

    try:  # try to open file
        openfile = open(filename, 'r')
    except:  # if couldn't open it
        print("ERROR: Could not open", filename)
        exit()

    pokemon = ['blank']
    p = {}
    headers = []
    headersDone = False
    for line in openfile:
        line = line.strip()
        line = line.split('\t')

        if not headersDone:  # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = re.sub('[^0-9a-zA-Z .-]+', '', h)  # get rid of random chars
                headers.append(h)  # append header to list
        else:  # if are past the headers
            if len(line) != len(headers):
                print("ERROR: Lengths of row and num of headers is not equal // row:", len(line), "| headers:",
                      len(headers))
                exit()

            i = 0
            for l in line:
                try:
                    p[headers[i]] = float(l)
                except:
                    p[headers[i]] = l
                i += 1

            try:
                pokemon.append(p.copy())
            except:
                print("ERROR: Keyerror; expected", headers[i])
                openfile.close()
                exit()
            p = {}

    openfile.close()  # close file
    print("Loading complete. Loaded", len(pokemon) - 1, "pokemon.\n")

    return pokemon
