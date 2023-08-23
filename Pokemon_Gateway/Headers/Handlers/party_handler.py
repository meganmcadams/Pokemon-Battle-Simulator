import random
import typing

from Headers import Party
from Headers import SavedPokemon
from Headers import Trainer
from Headers.tools import option, subheader


def validate_parties(party1, party2):
    parties = Party.get_all()
    try:  # try turning into ints
        party1 = int(party1)
        party2 = int(party2)
    except Exception:
        print("ERROR: One or more of the inputs was not an integer")
        return -1, -1, -1, -1

    if party1 >= len(parties) or party2 >= len(parties):  # if id of party is not in parties
        print("ERROR: One or more of the ids given aren't in parties")
        return -1, -1, -1, -1

    # set parties to what they actually are instead of the id
    party1 = parties[party1]
    party2 = parties[party2]

    party1_pokemon = party1.pokemon
    party2_pokemon = party2.pokemon

    for p in party1_pokemon:
        if p in party2_pokemon:
            print("ERROR: Pokemon overlap between parties")
            return -1, -1, -1, -1

    return party1, party2, party1_pokemon, party2_pokemon


def get_party_order(party1: Party, party2: Party) -> typing.Union[list[SavedPokemon], typing.Literal[-1]]:
    subheader("Party Order")

    # party_order holds all pokemon in all parties, will be sorted later
    party_order = [value for value in party1.pokemon] + [value for value in party2.pokemon]

    # Menu
    option(0, "Use speed of Pokemon")
    option(1, "Manually enter order")
    option(2, "Random order")
    option(3, "Cancel")
    inp = input("--> ")

    try:  # try to turn inp into an integer
        inp = int(inp)
    except Exception:
        inp = -1

    if inp == 0:
        party_order.sort(key=lambda x: x.stats.speed, reverse=True)  # sort by speed
        return party_order

    elif inp == 1:  # Manually enter
        options = []  # options from party_order
        for p in party_order:  # print pokemon in party_order so user knows what their options are
            try:
                owner = str(Trainer.get_trainer(p.tid).name) + "'s"
            except Exception:
                owner = "Wild"
            print(f"{owner}'s {p.name} ({p.id})")
            options.append(str(p.id))
        print("")  # print newline

        order_inp = []

        print("Input the Pokemon's IDs in the order that you'd like them to go.")

        for i in range(len(party_order)):
            order_inp.append(input(str(i + 1) + ": "))
        print("")  # print newline

        # ugh, why aren't sets ordered, this is so annoying
        done = []  # store done order to prevent repeats

        i = 0
        while i < len(order_inp):  # check if it's in party_order
            if order_inp[i] not in options:  # if isn't in options that we got earlier from party_order
                print("ERROR:", order_inp[i], "not found in party_order\n")
                return -1

            if order_inp[i] in done:  # if already done that one
                print("ERROR: You entered", order_inp[i], "more than once\n")
                return -1

            done.append(order_inp[i])  # append what we've done so we don't accidentally repeat
            order_inp[i] = SavedPokemon.get_pokemon(order_inp[i].id)


            i += 1

        return party_order

    elif inp == 2:  # Random order
        random.shuffle(party_order)  # shuffle the party order
        return party_order

    elif inp == 3:  # Cancel
        return -1

    else:
        print("ERROR:", inp, "was not an option or the input was not an integer")
        return -1
