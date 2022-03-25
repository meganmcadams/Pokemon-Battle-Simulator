import re

def load_move_levels(pokemon_num):

    print("Loading move levels...")

    filename = "Resources/move_levels.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    move_levels = ['blank']
    row = {}

    headersDone = False
    headers = []

    for line in openfile:
        line = line.split('\t')

        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = re.sub('[^0-9a-zA-Z .]+', '', h) # get rid of random chars
                headers.append(h) # append header to list
            if len(headers) < 3: # make sure there's at least three headers (pid, mid, and level)
                print("ERROR: Expected at least columns but got",len(headers))
                openfile.close()
                exit()

        else: # if are past the headers
            if int(line[0]) >= len(move_levels): # if we need to make a new row
                move_levels.append({}) # make new dict row

            try:
                move_levels[int(line[0])][int(line[2])].append(int(line[1])) # try to add move to pid's level list
            except:
                move_levels[int(line[0])][int(line[2])] = [] # declare list
                move_levels[int(line[0])][int(line[2])].append(int(line[1])) # now try adding

    openfile.close() # close file
    print("Loading complete. Loaded",(len(move_levels) - 1),"move levels.\n")

    if pokemon_num != len(move_levels) - 1: # make sure every pokemon is stored in move_levels
        print("ERROR: Number of move_levels does not equal number of Pokemon.")
        exit()

    return move_levels