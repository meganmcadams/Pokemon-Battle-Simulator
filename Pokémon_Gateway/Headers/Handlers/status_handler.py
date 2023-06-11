from Headers.tools import *
import random

def status_damage(pokemon, curr_pokemon): # handle status effects at end of cycle

    if curr_pokemon['Status'] != "": # if has a status, handle status effects
        if curr_pokemon['Status'] == "Burn" or curr_pokemon['Status'] == "Poison":
            print(pokemon[curr_pokemon['Pid']],"was hurt by its",curr_pokemon['Status'])
            curr_pokemon['Curr HP'] -= (int(curr_pokemon['HP']) * 0.05) # decrease health by 5%
            print(curr_pokemon['Curr HP'])
    return

def status_check(pokemon, move, opponent):
    add_status = True
    if move['Status'] == "":
        add_status = False
    elif opponent['Status'] != "":
        num = random.randrange(1,4) # 25% chance of yeeting the status
        if num == 1: # yeet the status
            print(pokemon[opponent['Pid']]['Name'],"is no longer afflicted with",opponent['Status'])
            opponent['Status'] = ""

    if add_status == True: # if can add a status
        try: # try splitting possible statuses into a list
            statuses = move['Status'].split(',')
        except: # if only one in list
            statuses = [move['Status']]

        i = random.randrange(0,len(statuses)) # pick random status from list
        min_num = random.randrange(1,100)
        num = float(move['Status Chance']) * 100 # get chance of status effect

        if num >= min_num:
            print(pokemon[opponent['Pid']]['Name'], "was afflicted with",statuses[i])
            opponent['Status'] = statuses[i]
            return
        else:
            return