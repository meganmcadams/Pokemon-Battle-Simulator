import os.path
import re
from ..tools import *


def load_move_levels(pokemon_num):
    print("Loading move levels...")

    filename = os.path.join("Resources", "move_levels.txt")

    try:  # try to open file
        openfile = open(filename, 'r')
    except Exception:  # if couldn't open it
        print("ERROR: Could not open", filename)
        exit()

    move_levels = {}

    headers_done = False
    headers = []

    for line in openfile:
        line = line.split('\t')
        i = 0
        for _ in line:  # fix the items in the line
            line[i] = str(line[i]).strip()
            line[i] = correct_type(line[i])  # fix type to int, float, or string
            i += 1

        if not headers_done:  # if haven't stored headers yet
            headers_done = True
            for h in line:
                h = re.sub('[^0-9a-zA-Z .]+', '', h)  # get rid of random chars
                headers.append(h)  # append header to list
            if len(headers) < 3:  # make sure there's at least three headers (pid, mid, and level)
                print("ERROR: Expected at least columns but got", len(headers))
                openfile.close()
                exit()

        else:  # if are past the headers
            pid = line[0]
            mid = line[1]
            level = line[2]

            if int(pid) not in move_levels.keys():  # if we need to make a new row
                move_levels[pid] = {}  # make new dict row

            try:
                move_levels[pid][level].append(mid)  # try to add move to pid's level list
            except Exception:
                move_levels[pid][level] = []  # declare list
                move_levels[pid][level].append(mid)  # now try adding

    openfile.close()  # close file
    print("Loading complete. Loaded", len(move_levels), "move levels.\n")

    if pokemon_num != len(move_levels):  # make sure every pokemon is stored in move_levels
        print("ERROR: Number of move_levels does not equal number of Pokemon.")
        exit()

    return move_levels
