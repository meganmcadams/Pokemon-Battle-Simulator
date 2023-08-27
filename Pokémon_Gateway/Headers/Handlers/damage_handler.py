import random

def damage(pokemon, move, attacker, opponent, weather):

    if move['Power'] == 0 or move['Category'] == "Status": # if the move does nothing
        return

    critical_chance = 0.05 # default critical hit chance to 5%
    critical = 1 # default critical to no increase
    min_num = random.randrange(1,100)
    num = critical_chance * 100
    if num >= min_num:
        critical = 1.5

    stab = 1
    if move['Type'] is pokemon[int(attacker['Pid'])]['Type1'] or move['Type'] is pokemon[int(attacker['Pid'])]['Type2']:
        stab = 1.5

    burn = 1
    if opponent['Status'] == "Burn" and move['Category'] == "Physical":
        burn = 0.5

    weather_bonus = 1
    if weather != "": # if weather is not default
        if weather is pokemon[int(attacker['Pid'])]['Type1'] or weather is pokemon[int(attacker['Pid'])]['Type2']:
            weather_bonus = 1.5

    opponent_type = pokemon[int(opponent['Pid'])][move['Type']]

    rng = random.randrange(85,100) / 100

    part1 = ((int(attacker['Level']) * 2) / 5) + 2

    if move['Category'] == "Special":
        part2 = int(move['Power']) * (int(attacker['Curr Sp Attack']) / int(opponent['Curr Sp Defense']))
    else:
        part2 = int(move['Power']) * (int(attacker['Curr Attack']) / int(opponent['Curr Defense']))

    left = ((part1 * part2) / 50) + 2
    damage = left * weather_bonus * critical * rng * stab * burn * opponent_type
    
    print(move['Name'],"did",round(damage),"damage!")
    opponent['Curr HP'] -= round(damage)

    if opponent_type < 1:
        print("It wasn't very effective...")
    elif opponent_type > 1:
        print("It was very effective!")
