import random

from Headers import Move, SavedPokemon


def damage(move: Move, attacker: SavedPokemon, opponent: SavedPokemon, weather):
    if move.power == 0 or move.category == "Status":  # if the move does nothing
        return

    critical_chance = 0.05  # default critical hit chance to 5%
    critical = 1  # default critical to no increase
    min_num = random.randrange(1, 100)
    num = critical_chance * 100
    if num >= min_num:
        critical = 1.5

    stab = 1
    if move.type in attacker.types:
        stab = 1.5

    burn = 1
    if opponent.status == "Burn" and move.category == "Physical":
        burn = 0.5

    weather_bonus = 1.5 if weather == move.type else 1

    opponent_type = opponent.type_effectiveness[move.type]

    rng = random.randrange(85, 100) / 100

    part1 = ((attacker.level * 2) / 5) + 2

    if move.category == "Special":

        part2 = move.power * (attacker.curr_stats.sp_attack / opponent.curr_stats.sp_defense)
    else:
        part2 = move.power * (attacker.curr_stats.attack / opponent.curr_stats.defense)

    left = ((part1 * part2) / 50) + 2
    damage_amount = round(left * weather_bonus * critical * rng * stab * burn * opponent_type)

    print(f"{move.name} did {damage_amount} damage!")
    opponent.curr_stats.hp -= damage_amount

    if opponent_type < 1:
        print("It wasn't very effective...")
    elif opponent_type > 1:
        print("It was very effective!")
