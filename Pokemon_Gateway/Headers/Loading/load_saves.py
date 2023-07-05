import re

def load_saves():

    print("Loading stored pokemon...")

    filename = "Saves/pokemon.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    stored_pokemon = []
    headers = []
    headersDone = False

    for line in openfile:
        line = line.split('\t')
        
        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = h.strip()
                h = re.sub('[^0-9a-zA-Z .-]+', '', h) # get rid of random chars
                headers.append(h) # append header to list
            if len(headers) < 3: # make sure there's at least three headers (pid, mid, and level)
                print("ERROR: Expected at least columns but got",len(headers))
                openfile.close()
                exit()

        else: # if are past the headers
            temp = {} # make temp to store later

            i = 0
            for l in line: # for item in line
                l = l.strip()
                try: # try storing as an int
                    temp[headers[i]] = int(l)
                except: # if can't store as an int, store as a string
                    temp[headers[i]] = l
                i += 1
            
            if int(len(stored_pokemon)) != int(temp['ID']): # if index doesn't match expected (lid)
                    print("ERROR: Was not at the correct index for stored_pokemon. Expected",line[0],"but got",len(stored_pokemon))
                    print(stored_pokemon)
                    openfile.close()
                    exit()

            stored_pokemon.append(temp.copy()) # add copy

    openfile.close() # close file
    print("Loading complete. Loaded",(len(stored_pokemon)),"stored pokemon.\n")

    return stored_pokemon

def load_stored_pokemon():

    print("Loading stored pokemon...")

    filename = "Saves/pokemon.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    stored_pokemon = []
    headers = []
    headersDone = False

    for line in openfile:
        line = line.split('\t')
        
        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = h.strip()
                h = re.sub('[^0-9a-zA-Z .-]+', '', h) # get rid of random chars
                headers.append(h) # append header to list
            if len(headers) < 3: # make sure there's at least three headers (pid, mid, and level)
                print("ERROR: Expected at least columns but got",len(headers))
                openfile.close()
                exit()

        else: # if are past the headers
            temp = {} # make temp to store later

            i = 0
            for l in line: # for item in line
                l = l.strip()
                try: # try storing as an int
                    temp[headers[i]] = int(l)
                except: # if can't store as an int, store as a string
                    temp[headers[i]] = l
                i += 1
            
            if int(len(stored_pokemon)) != int(temp['ID']): # if index doesn't match expected (lid)
                    print("ERROR: Was not at the correct index for stored_pokemon. Expected",line[0],"but got",len(stored_pokemon))
                    print(stored_pokemon)
                    openfile.close()
                    exit()

            stored_pokemon.append(temp.copy()) # add copy

    openfile.close() # close file
    print("Loading complete. Loaded",(len(stored_pokemon)),"stored pokemon.\n")

    return stored_pokemon

def load_trainers():

    print("Loading trainers...")

    filename = "Saves/trainers.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    trainers = []
    headers = []
    headersDone = False

    for line in openfile:
        line = line.split('\t')
        
        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = h.strip()
                h = re.sub('[^0-9a-zA-Z .-]+', '', h) # get rid of random chars
                headers.append(h) # append header to list
            if len(headers) < 3: # make sure there's at least three headers (pid, mid, and level)
                print("ERROR: Expected at least columns but got",len(headers))
                openfile.close()
                exit()

        else: # if are past the headers
            temp = {} # make temp to store later

            i = 0
            for l in line: # for item in line
                l = l.strip()
                try: # try storing as an int
                    temp[headers[i]] = int(l)
                except: # if can't store as an int, store as a string
                    temp[headers[i]] = l
                i += 1
            
            if int(len(trainers)) != int(line[0]): # if index doesn't match expected (lid)
                    print("ERROR: Was not at the correct index for trainers. Expected",line[0],"but got",len(trainers))
                    print(trainers)
                    openfile.close()
                    exit()

            trainers.append(temp.copy()) # add copy

    openfile.close() # close file
    print("Loading complete. Loaded",(len(trainers)),"trainers.\n")

    return trainers

def load_parties():

    print("Loading parties...")

    filename = "Saves/parties.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    parties = []
    headers = []
    headersDone = False

    for line in openfile:
        line = line.split('\t')
        
        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = h.strip()
                h = re.sub('[^0-9a-zA-Z .-]+', '', h) # get rid of random chars
                headers.append(h) # append header to list
            if len(headers) < 3: # make sure there's at least three headers (pid, mid, and level)
                print("ERROR: Expected at least columns but got",len(headers))
                openfile.close()
                exit()

        else: # if are past the headers
            temp = {} # make temp to store later

            i = 0
            for l in line: # for item in line
                l = l.strip()
                try: # try storing as an int
                    temp[headers[i]] = int(l)
                except: # if can't store as an int, store as a string
                    temp[headers[i]] = l
                i += 1
            
            if int(len(parties)) != int(line[0]): # if index doesn't match expected (lid)
                    print("ERROR: Was not at the correct index for parties. Expected",line[0],"but got",len(parties))
                    print(parties)
                    openfile.close()
                    exit()

            parties.append(temp.copy()) # add copy

    openfile.close() # close file
    print("Loading complete. Loaded",(len(parties)),"parties.\n")

    return parties