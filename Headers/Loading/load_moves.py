import re

def load_moves():

    print("Loading moves...")

    filename = "Resources/moves.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    moves = []
    moves.append('blank') # set index 0 to blank so id numbers can match; they start at 1
    m = {}
    headers = []
    headersDone = False
    for line in openfile:
        line = line.split('\t')
        
        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = re.sub('[^0-9a-zA-Z .]+', '', h) # get rid of random chars
                headers.append(h) # append header to list
        else: # if are past the headers
            if len(line) != len(headers):
                print("ERROR: Lengths of row and num of headers is not equal // row:",len(line),"| headers:",len(headers))
                exit()
            
            i = 0
            for l in line:
                m[headers[i]] = l
                i += 1

            try:
                moves.append(m.copy())
            except:
                print("ERROR: Keyerror; expected",headers[i])
                openfile.close()
                exit()
            m = {}


    openfile.close() # close file
    print("Loading complete. Loaded",len(moves),"moves.\n")

    return moves