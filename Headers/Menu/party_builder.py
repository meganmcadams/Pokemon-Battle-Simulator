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
        list_parties(parties)
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

    party = {}
    party['ID'] = len(parties)
    party['Name'] = name
    party['Pokemon'] = pokemon
    parties.append(party)

def delete_party(parties):
    party_id = input("ID (of party to delete): ")
    print("") # print newline

    try: # turn party_id into an integer
        party_id = int(party_id)
    except:
        party_id = -1

    try:
        del parties[party_id]
    except:
        print("ERROR: Could not remove party. Party may not exist.")
        return
    print("Party",party_id,"was successfully deleted.")

def list_parties(parties):
    if len(parties) < 1: # if there aren't any parties to print
        print("ERROR: There are",len(parties),"parties.")
        return

    for party in parties: # for every party
        for key in party: # for col in party
            print(key,": ",party[key],sep="") # print key's contents
        print("") # print newline