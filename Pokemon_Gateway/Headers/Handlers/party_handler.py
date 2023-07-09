from catch_handler import *


def validate_parties(pokemon, parties, party1, party2):
    try:  # try turning into ints
        party1 = int(party1)
        party2 = int(party2)
    except:
        print("ERROR: One or more of the inputs was not an integer")
        return -1, -1, -1, -1

    if party1 >= len(parties) or party2 >= len(parties):  # if id of party is not in parties
        print("ERROR: One or more of the ids given aren't in parties")
        return -1, -1, -1, -1

    # set parties to what they actually are instead of the id
    party1 = parties[party1]
    party2 = parties[party2]

    try:  # try breaking into list
        party1_pokemon = party1['Pokemon'].split(',')
    except:  # if only 1 pokemon
        party1_pokemon = [party1['Pokemon']]

    try:  # try breaking into list
        party2_pokemon = party2['Pokemon'].split(',')
    except:  # if only 1 pokemon
        party2_pokemon = [party2['Pokemon']]

    for p in party1_pokemon:
        if p in party2_pokemon:
            print("ERROR: Pokemon overlap between parties")
            return -1, -1, -1, -1

    i = 0
    while i < len(party1_pokemon):
        party1_pokemon[i] = pokemon[int(party1_pokemon[i])]  # set pokemon to actual pokemon, not pid
        i += 1

    i = 0
    while i < len(party2_pokemon):
        party2_pokemon[i] = pokemon[int(party2_pokemon[i])]  # set pokemon to actual pokemon, not pid
        i += 1

    return party1, party2, party1_pokemon, party2_pokemon


def get_party_order(trainers, pokemon, stored_pokemon, party1_pokemon, party2_pokemon):
    subheader("Party Order")

    party_order = []  # declare party order as list

    i = 0
    for p in party1_pokemon:  # store pokemon from party1 into party_order
        party_order.append(party1_pokemon[i])
        i += 1

    i = 0
    for p in party2_pokemon:  # store pokemon from party2 into party_order
        party_order.append(party2_pokemon[i])
        i += 1

    party_order_names = {}  # declare names of party pokemon
    for p in party_order:  # print pokemon in party_order so user knows what their options are
        try:
            owner = str(trainers[int(p['Tid'])]['Name']) + "'s"
        except:
            owner = "Wild"
        party_order_names[int(p['ID'])] = str(owner + " " + str(pokemon[p['Pid']]['Name']) + " (" + str(p['ID']) + ")")

    # Menu
    option(0, "Use speed of Pokemon")
    option(1, "Manually enter order")
    option(2, "Random order")
    option(3, "Cancel")
    inp = input("--> ")

    try:  # try to turn inp into an integer
        inp = int(inp)
    except:
        inp = -1

    if inp == 0:
        print("Not configured")
        return -1, -1

    elif inp == 1:  # Manually enter
        options = []  # options from party_order
        for p in party_order:  # print pokemon in party_order so user knows what their options are
            print(party_order_names[p['ID']])
            options.append(str(p['ID']))
        print("")  # print newline

        order_inp = []

        print("Input the Pokemon's IDs in the order that you'd like them to go.")

        i = 0
        for p in party_order:
            order_inp.append(input(str(i + 1) + ": "))
            i += 1
        print("")  # print newline

        done = []  # store done order_inps to prevent repeats

        i = 0
        while i < len(order_inp):  # check if it's in party_order
            if order_inp[i] not in options:  # if isn't in options that we got earlier from party_order
                print("ERROR:", order_inp[i], "not found in party_order\n")
                return -1, -1

            if order_inp[i] in done:  # if already done that one
                print("ERROR: You entered", order_inp[i], "more than once\n")
                return -1, -1

            done.append(order_inp[i])  # append what we've done so we don't accidentally repeat
            order_inp[i] = stored_pokemon[int(order_inp[i])]  # set to pokemon instead of id

            i += 1

        return party_order_names, party_order

    elif inp == 2:  # Random order
        options = []
        for p in party_order:  # copy party order to options
            options.append(p)
        party_order = []  # reset party order

        while len(options) > 0:  # while there are more pokemon to put in the party order
            p = random.choice(options)
            party_order.append(p)
            options.remove(p)

        return party_order_names, party_order

    elif inp == 3:  # Cancel
        return -1, -1

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")
        return -1, -1
