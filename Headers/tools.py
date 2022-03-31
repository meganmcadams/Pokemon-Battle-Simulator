from re import X

def header(text):
    text_size = len(text)
    print("") # print newline

    if text_size >= 70:
        print(text)
    else:

        header_size = (70 - text_size) / 2

        i = 0
        while i < header_size: # print left lines
            print('-',end='')
            i += 1

        print(text,end='') # print header

        i = 0
        while i < header_size: # print right lines
            print('-',end='')
            i += 1

        print('') # newline

def subheader(text):
    text_size = len(text)
    print("") # print newline
    if text_size >= 20:
        print("-" + text)
    else:

        header_size = (15 - text_size)

        i = 0
        while i < header_size: # print left lines
            print('-',end='')
            i += 1

        print(text) # print subheader

def option(num, text):
    temp = text; # store text
    text = "    | " + str(num) + ": " + str(temp)
    print(text)

def print_list(items):
    if len(items) < 1: # if there aren't any items to print
        print("ERROR: There are",len(items),"items.")
        return

    for item_key in items.keys(): # for every item
        for key in items[item_key]: # for col in item
            print(key,": ",items[item_key][key],sep="") # print key's contents
        print("") # print newline

def get_next_id(items):
    keylist = items.keys()
    keylist = list(keylist)
    keylist.sort()
    
    if keylist[-1] == len(items) - 1: # if last key is equal to length of items
        return keylist[-1] + 1

    prev = -1
    for key in keylist:
        if key != prev + 1:
            return prev + 1

    return len(items)


def correct_type(item): # fix the type, if possible
    try:
        item = int(item)
    except:
        try:
            item = float(item)
        except:
            item = str(item)

    return item