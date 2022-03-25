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
    if len(items) < 1: # if there aren't any parties to print
        print("ERROR: There are",len(items),"items.")
        return

    for item in items: # for every item
        for key in item: # for col in item
            print(key,": ",item[key],sep="") # print key's contents
        print("") # print newline