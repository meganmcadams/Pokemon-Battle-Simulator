from Headers.tools import *

def battle_simulator(pokemon, stored_pokemon, parties):
    header("Battle Simulator")
    print_list(parties) # list existing parties
    party1 = input("Party 1: ")
    party2 = input("Party 2: ")

    try: # try turning into ints
        party1 = int(party1)
        party2 = int(party2)
    except:
        print("ERROR: One or more of the inputs was not an integer")
        return

    if party1 >= len(parties) or party2 >= len(parties): # if id of party is not in parties
        print("ERROR: One or more of the ids given aren't in parties")
        return

    # set parties to what they actually are instead of the id
    party1 = parties[party1]
    party2 = parties[party2]

