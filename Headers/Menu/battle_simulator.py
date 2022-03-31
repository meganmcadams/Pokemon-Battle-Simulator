from Headers.tools import *
from Headers.Handlers.party_handler import *
from Headers.Handlers.battle_handler import *
from Headers.Handlers.status_handler import *
from Headers.Handlers.damage_handler import *
from Headers.Handlers.level_handler import *

def battle_simulator(trainers, items, pokemon, stored_pokemon, parties, moves, to_next_level, move_levels):
    header("Battle Simulator")

    if len(parties) < 2: # if there are less than 2 parties
        print("ERROR: At least 2 parties are needed to run the battle simulator")
        return

    print_list(parties) # list existing parties
    party1 = input("Party 1: ")
    party2 = input("Party 2: ")

    party1, party2, party1_pokemon, party2_pokemon = validate_parties(stored_pokemon, parties, party1, party2) # validate the parties
    if party1 == -1: # if party validation was unsuccessful
        return

    party_order_names, party_order = get_party_order(trainers, pokemon, stored_pokemon, party1_pokemon, party2_pokemon)
    if party_order == -1: # if party order was unsuccessful
        return

    party1_copy = party1.copy()
    party2_copy = party2.copy()

    fainted_pokemon = [] # store fainted pokemon

    winner = -1 # default winner to no one
    cycle = 1
    weather = "" # default weather to none
    while True:
        turn = 1

        for curr_pokemon in party_order: # go through pokemon's turns one by one

            current_party = party2_copy # default
            opposing_party = party1_copy # default

            for p in party1_pokemon: # try to find curr_pokemon in party1_pokemon
                if p == curr_pokemon:
                    current_party = party1_copy
                    opposing_party = party2_copy
                    break

            if int(curr_pokemon['Curr HP']) > 0: # if the pokemon can do something and isn't dead

                subheader(current_party['Name'] + " | " + party_order_names[curr_pokemon['ID']] + " | " + str("Cycle " + str(cycle) + ", Turn " + str(turn)))

                curr_move = -1
                while curr_move == -3: # get move
                    curr_move = get_move(curr_pokemon, moves)

                if curr_move != -2: # if not pass

                    target = -1
                    while target == -1: # get target
                        target = get_target(pokemon, stored_pokemon, current_party, opposing_party)

                    if curr_move == -1: # throw pokeball
                        throw_pokeball(pokemon, items, trainers, current_party, opposing_party, target, curr_pokemon['Tid'])

                    if accuracy_check(curr_pokemon, curr_move) is True: # determine if it hits
                        stat_change_check(curr_move, curr_pokemon, target) # apply stat changes
                        status_check(pokemon, curr_move, target) # apply status effect
                        weather_check(curr_move, weather) # update weather

                    damage(pokemon, curr_move, curr_pokemon, target, weather) # dish out damage

                # end of if not pass

                # do a health check if the pokemon is dead or not if it did hit
            curr_health_check = health_check(party_order, party1_pokemon, party2_pokemon, party_order_names, fainted_pokemon)
                
            if curr_health_check == 0: # if no winner yet
                pass
            elif curr_health_check == 1: # party1 won
                print(party1['Name'],"won!")
                winner = party1_pokemon
                break
            elif curr_health_check == 2: # party2 won
                print(party2['Name'],"won!")
                winner = party2_pokemon
                break
            else:
                print("ERROR: Expected 0, 1, or 2 from health_check() but got",curr_health_check)
                return
            
                # level up check

            # end of if pokemon isn't dead

            

            turn += 1

        # check if there are any pokemon left, if there aren't then determine winner and break
        if winner != -1:
            if winner == party1_pokemon:
                loser = party2_pokemon
            else:
                loser = party1_pokemon
            break

        for p in party1_pokemon: # apply any status damage to party 1 pokemon
            status_damage(pokemon, p)

        for p in party2_pokemon: # apply any status damage to party 2 pokemon
            status_damage(pokemon, p)

        cycle += 1

    # evolution/level check
    exp(pokemon, winner, loser)

    # rewards if won

    for p in winner:
        #level_check(pokemon, p, to_next_level, move_levels, moves)
        #trainers[int(p['Tid'])]['Money'] += len(loser) * random.randrange(50,200)
        pass

    return