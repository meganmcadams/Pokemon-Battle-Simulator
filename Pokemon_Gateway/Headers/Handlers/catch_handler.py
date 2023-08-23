from Headers.tools import *


def throw_pokeball(pokemon, items, trainers, current_party, opposing_party, opposing_pokemon, tid):
    print("not done yet")

    option(0, "Success")
    option(1, "Failure")
    inp = correct_type(input("--> "))

    if inp == 0:
        catch_pokemon(pokemon, opposing_pokemon, trainers, tid)
        return 1
    else:
        print("1... 2... Oh no! The Pokemon broke free!")
        return -1

    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE


def get_balls(items, trainer):
    try:
        trainer_items = trainer['Items'].split(',')
    except Exception:
        trainer_items = [trainer['Items']]

    balls = []

    for i in trainer_items:
        correct_type(i)
        try:
            curr_item = items[i]
            if "Ball" in curr_item['Name']:
                balls.append(curr_item)
        except Exception:
            pass

    return balls


def catch_pokemon(pokemon, caught_pokemon, trainers, tid):
    print("1... 2... 3... Click!", opposing_pokemon['Name'], "was caught!")
    if trainers[tid]['Pokemon'] == "":
        trainers[tid]['Pokemon'] = str(opposing_pokemon['ID'])
    else:
        trainers[tid]['Pokemon'] += "," + str(opposing_pokemon['ID'])
