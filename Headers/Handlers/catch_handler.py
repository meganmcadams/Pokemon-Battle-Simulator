from Headers.tools import *
import random

def throw_pokeball(pokemon, items, trainers, current_party, opposing_party, opposing_pokemon, tid):
    print("not done yet")

    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE
    # THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE THIS IS NOT DONE

def get_balls(items, trainer):
    try:
        trainer_items = trainer['Items'].split(',')
    except:
        trainer_items = [trainer['Items']]

    balls = []

    for i in trainer_items:
        correct_type(i)
        try:
            curr_item = items[i]
            if "Ball" in curr_item['Name']:
                balls.append(curr_item)

    return balls

def catch_pokemon(pokemon, caught_pokemon, trainers, tid):
    print("1... 2... 3... Click!",opposing_pokemon['Name'],"was caught!")
    if trainers[tid]['Pokemon'] == "":
        trainers[tid]['Pokemon'] = str(opposing_pokemon['ID'])
    else:
        trainers[tid]['Pokemon'] += "," + str(opposing_pokemon['ID'])