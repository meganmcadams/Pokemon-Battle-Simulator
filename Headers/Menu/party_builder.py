from Headers.tools import *

def party_builder(pokemon, stored_pokemon, parties):
    print("") # print newline
    header("Party Builder")
    option(0, "Create Party")
    option(1, "Delete Party")
    option(2, "List Parties")
    option(3, "Exit")
    inp = input("--> ")
    print("") # print newline

    try: # try turning inp into an integer
        inp = int(inp)
    except: # if not an integer
        inp = -1 # set to -1 to classify as a wrong input

    if inp == 0: # Create Party
        create_party(stored_pokemon, parties)

    elif inp == 1: # Delete Party
        delete_party(parties)

    elif inp == 2: # List Parties
        print_list(parties)

    elif inp == 3: # Exit
        return

    else: # incorrect input
        print("ERROR:",inp,"was not an option or the input was not an integer.")

    party_builder(pokemon, stored_pokemon, parties) # recursive call to continue indefinitely until exit
    return # return after recursive call

def create_party(stored_pokemon, parties):
    name = input("Name: ")
    pokemon = input("Pokemon (comma-separated): ")
    print("") # print newline

    pokemon_split = pokemon.split(',') # split pokemon by commas for error checking
    for p in pokemon_split:
        try: # try turning to int
            p = int(p)
        except:
            print("ERROR:",p,"is not an integer")
            return
        if p >= len(stored_pokemon): # check if it is in the stored pokemon
            print("ERROR:",p,"is not the id of a valid stored pokemon")
            return

    party = {}
    party['ID'] = len(parties)
    party['Name'] = name
    party['Pokemon'] = pokemon
    parties.append(party)

    print("Party",len(parties) - 1,"successfully created")

def delete_party(parties):
    print_list(parties)
    print("Which party would you like to delete (-1 to cancel)?")
    to_delete = correct_type(input("--> "))
    if to_delete == -1:
        print("Action cancelled.")
    else:
        try:
            del parties[to_delete]
            print(to_delete,"was successfully deleted")
        except:
            print("ERROR: Could not delete",to_delete)