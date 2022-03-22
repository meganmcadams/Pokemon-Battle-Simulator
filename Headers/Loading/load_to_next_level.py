import re

def load_to_next_level():

    print("Loading levels...")

    filename = "Resources/to_next_level.txt"

    try: # try to open file
        openfile = open(filename, 'r')
    except: # if couldn't open it
        print("ERROR: Could not open",filename)
        exit()

    to_next_level = ['blank']
    headers = []
    headersDone = False

    for line in openfile:
        line = line.split('\t')
        
        if not headersDone: # if haven't stored headers yet
            headersDone = True
            for h in line:
                h = h.strip()
                h = re.sub('[^0-9a-zA-Z ]+', '', h) # get rid of random chars
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
                if i != 0: # if is not the level
                    temp[headers[i]] = int(l)
                i += 1
            
            if int(len(to_next_level)) != int(line[0]): # if index doesn't match expected (lid)
                    print("ERROR: Was not at the correct index for to_next_level. Expected",line[0],"but got",len(to_next_level))
                    print(to_next_level)
                    openfile.close()
                    exit()

            to_next_level.append(temp.copy()) # add copy

    openfile.close() # close file
    print("Loading complete. Loaded",(len(to_next_level) - 1),"levels.\n")

    return to_next_level