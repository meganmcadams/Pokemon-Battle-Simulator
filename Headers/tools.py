def header(text):
    text_size = len(text)
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

def option(num, text):
    temp = text; # store text
    text = "    | " + str(num) + ": " + str(temp)
    print(text)