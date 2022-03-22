import re

def load_move_levels(pokemon_num):

    print("Loading move levels...")

    filename = "Resources/move_levels.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    move_levels = []
    move_levels.append('blank') # set index 0 to blank so id numbers can match; they start at 1
    curr = ''
    headers = []
    headersDone = False

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
            if line[0] == curr: # if we're still on the current pokemon
                move_levels[int(line[0])][int(line[1])] = int(line[2]) # set move_levels[pid][mid] equal to level
            else:
                move_levels.append({}) # append a blank dictionary to the end

                if int(len(move_levels) - 1) != int(line[0]): # if index doesn't match expected (pid)
                    print("ERROR: Was not at the correct index for move_levels. Expected",line[0],"but got",len(move_levels) - 1)
                    openfile.close()
                    exit()

                line[2] = line[2].strip()
                move_levels[int(line[0])][int(line[1])] = int(line[2]) # set move_levels[pid][mid] equal to level
                curr = line[0]

    openfile.close() # close file
    print("Loading complete. Loaded",(len(move_levels) - 1),"move levels.\n")

    if pokemon_num != len(move_levels) - 1: # make sure every pokemon is stored in move_levels
        print("ERROR: Number of move_levels does not equal number of Pokemon.")
        exit()

    return move_levels