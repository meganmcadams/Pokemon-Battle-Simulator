import os
import re
from ..tools import *


def load(filename, foldername):  # loads file as dictionary of lists, first column needs to be ids

    item = filename
    print("Loading ", filename, "...", sep="")

    filename = os.path.join(str(foldername), str(filename) + ".txt")

    try:  # try to open file
        openfile = open(filename, 'r', encoding="ISO-8859-1")  # this encoding is needed for some unix systems
    except Exception:  # if couldn't open it
        print("ERROR: Could not open", filename)
        exit()

    col = {}  # dictionary of ids
    row = {}  # dictionary of headers to put into columns
    headers = []  # list of headers to use as keys for rows
    headers_done = False  # if we've stored the headers yet

    for line in openfile:
        line = line.split('\t')  # split line into list of items

        if not headers_done:  # if haven't stored headers yet
            headers_done = True
            for h in line:
                h = h.strip()
                h = re.sub('[^0-9a-zA-Z .]+', '', h)  # get rid of random chars
                headers.append(h)  # append header to list
        else:  # if are past the headers
            if len(line) != len(headers):  # if columns in row isn't equal to num of headers
                print("ERROR: Lengths of row and num of headers is not equal // row:", len(line), "| headers:",
                      len(headers))
                openfile.close()
                exit()

            i = 0
            for word in line:  # for item in line
                word = correct_type(word.strip())
                row[headers[i]] = word  # store contents into appropriate column
                i += 1

            # end of for l in line:

            id_key = correct_type(line[0])  # get id
            col[id_key] = row.copy()  # store copy of row into col using the first col as the id

        # end of else: # if are past the headers

    # end of for line in openfile:

    openfile.close()
    print("Loading complete. Loaded ", len(col), " ", item, ".\n", sep="")

    return col
