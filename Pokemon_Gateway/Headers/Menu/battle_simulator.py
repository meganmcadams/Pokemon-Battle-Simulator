from Headers.Handlers.battle_handler import *
from Headers.Handlers.catch_handler import throw_pokeball
from Headers.Handlers.damage_handler import *
from Headers.Handlers.level_handler import *
from Headers.Handlers.party_handler import *
from Headers.Handlers.status_handler import *
from Headers.tools import header, print_list


# noinspection PyTypeChecker
def battle_simulator(move_levels):
    header("Battle Simulator")

    if len(Party.get_all()) < 2:  # if there are less than 2 parties
        print("ERROR: At least 2 parties are needed to run the battle simulator")
        return

    print_list(Party.as_dicts())  # list existing parties
    party1_id = input("Party 1: ")
    party2_id = input("Party 2: ")

    party1 = Party.get_party(int(party1_id))
    party2 = Party.get_party(int(party2_id))

    # party1_id, party2_id, party1, party2 = validate_parties(stored_pokemon, parties, party1_id,
    #                                                                   party2_id)  # validate the parties
    if party1_id == -1:  # if party validation was unsuccessful
        return

    party_order = get_party_order(party1, party2)
    if party_order == -1:  # if party order was unsuccessful
        return

    party1_copy = copy.deepcopy(party1)
    party2_copy = copy.deepcopy(party2)

    fainted_pokemon = []  # store fainted pokemon

    winner: Party = -1  # default winner to no one
    cycle = 1
    weather = ""  # default weather to none

    health_check(party_order, party1, party2, fainted_pokemon)  # make sure no pokemon start fainted

    while True:
        turn = 1

        for curr_pokemon in party_order:  # go through pokemon's turns one by one

            current_party = party2_copy  # default
            opposing_party = party1_copy  # default

            for p in party1:  # try to find curr_pokemon in party1_pokemon
                if p == curr_pokemon:
                    current_party = party1_copy
                    opposing_party = party2_copy
                    break

            if int(curr_pokemon.curr_stats.hp) > 0:  # if the pokemon can do something and isn't dead
                subheader(f"{current_party.name} | {curr_pokemon.id} | Cycle {cycle}, Turn {turn}")

                curr_move = -3
                while curr_move == -3:  # get move
                    curr_move = get_move(curr_pokemon)

                if curr_move != -2:  # if not pass

                    target = -1
                    while target == -1:  # get target
                        target = get_target(party_order, opposing_party)

                    if curr_move == -1:  # throw pokeball
                        throw_pokeball(target, curr_pokemon.tid)

                    if accuracy_check(curr_pokemon, curr_move) is True:  # determine if it hits
                        stat_change_check(curr_move, curr_pokemon, target)  # apply stat changes
                        status_check(curr_move, target)  # apply status effect
                        weather = weather_check(curr_move, weather)  # update weather

                    damage(curr_move, curr_pokemon, target, weather)  # dish out damage
                # end of if not pass

            # do a health check if the pokemon is dead or not if it did hit
            curr_health_check = health_check(party_order, party1, party2, fainted_pokemon)

            if curr_health_check == 0:  # if no winner yet
                pass
            elif curr_health_check == 1:  # party1 won
                print(party1.name, "won!")
                winner = party1
                break
            elif curr_health_check == 2:  # party2 won
                print(party2.name, "won!")
                winner = party2
                break
            else:
                print("ERROR: Expected 0, 1, or 2 from health_check() but got", curr_health_check)
                return

            # end of if pokemon isn't dead

            turn += 1

        # check if there are any pokemon left, if there aren't then determine winner and break
        if winner != -1:
            if winner == party1:
                loser = party2
            else:
                loser = party1
            break

        for p in party1:  # apply any status damage to party 1 pokemon
            status_damage(p)

        for p in party2:  # apply any status damage to party 2 pokemon
            status_damage(p)

        cycle += 1

    # evolution/level check
    exp(winner, loser)

    # rewards if won
    money = len(loser.pokemon) + (loser[0].level * 2) * random.randrange(50, 200)
    for p in winner:
        level_check(p, move_levels)
        try:  # try to give money to the trainer, if any
            Trainer.get_trainer(p.tid).money += money
        except Exception:
            pass

    return
