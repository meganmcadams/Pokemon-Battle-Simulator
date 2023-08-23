import random

from Headers import Move
from Headers import Party
from Headers import SavedPokemon
from Headers.tools import option, subheader, format_name, correct_type


def get_move(pokemon: SavedPokemon):
    subheader("Move")

    # try:  # try breaking into list
    #     pokemon_moves = pokemon['Moves'].split(',')
    # except Exception:  # if only 1 pokemon
    #     pokemon_moves = [pokemon['Moves']]

    # i = 0
    # for m in pokemon.moves:  # set pokemon_moves[i] to actual move info
    #     try:  # try to find move info
    #         pokemon.moves[i] = moves[int(pokemon.moves[i])]
    #     except Exception:
    #         print("ERROR: Could not find", pokemon.moves[i], "in moves")
    #         return -3  # error
    #
    #     i += 1

    options = [-2, -1]
    option(-2, "Pass")
    option(-1, "Throw Pokeball")

    i = 0
    for m in pokemon.moves:  # print move options
        option(i, f"{m.name} ({m.description})")
        options.append(i)
        i += 1

    inp = input("--> ")

    try:  # try turning to integer
        inp = int(inp)
    except Exception:
        print(f"ERROR: {inp} was not an option")
        return -3  # error

    if inp not in options:
        print(f"ERROR: {inp} was not an option")
        return -3  # error

    if inp == -1 or inp == -2:  # if pass or throw pokeball
        return inp
    return pokemon.moves[inp]  # else return move


def accuracy_check(curr_pokemon: SavedPokemon, move: Move):  # determine if a move hits or misses
    if int(curr_pokemon.flinched) == 1:  # flinch check
        curr_pokemon.flinched = 0
        print(curr_pokemon.name, "flinched!")
        return False

    if curr_pokemon.status == "Sleep" or curr_pokemon.status == "Freeze":
        print(curr_pokemon.name, "is afflicted by", curr_pokemon.status)
        return False

    if curr_pokemon.status == "Confusion":
        num = random.randrange(1, 2)  # 50% chance to be hurt by confusion
        if num == 1:
            print(curr_pokemon.name, "was hurt by its confusion!")
            # todo: damage calc based on current attack stat
            curr_pokemon.curr_hp -= (int(curr_pokemon.stats.hp) * 0.05)  # decrease health by 5%
            return False
        else:
            print(curr_pokemon.name, "pushed through its confusion.")

    if curr_pokemon.status == "Paralysis":
        num = random.randrange(1, 2)  # 50% to be paralyzed
        if num == 1:
            print(curr_pokemon.name, "is paralyzed!")
            return False

    # if passed the status check, check if the move misses or not
    min_num = random.randrange(1, 100)
    num = float(move.accuracy) * 100

    if num >= min_num:
        return True
    else:
        print(str(move.name + " missed!"))
        return False


def stat_change_check(move: Move, attacker: SavedPokemon, opponent: SavedPokemon) -> None:
    # opponent stat changes
    opponent.curr_stats.speed += int(move.o_speed)
    opponent.curr_stats.attack += int(move.o_attack)
    opponent.curr_stats.defense += int(move.o_defense)
    opponent.curr_stats.sp_attack += int(move.o_sp_attack)
    opponent.curr_stats.sp_defense += int(move.o_sp_defense)

    # attacker stat changes
    attacker.curr_stats.speed += int(move.p_speed)
    attacker.curr_stats.attack += int(move.p_attack)
    attacker.curr_stats.defense += int(move.p_defense)
    attacker.curr_stats.sp_attack += int(move.p_sp_attack)
    attacker.curr_stats.sp_defense += int(move.p_sp_defense)

    # flinch check
    # todo: update flinch check to use move flinch rates
    if int(move.flinch) > 0:
        num = random.randrange(1, 2)
        if num == 1:
            opponent.flinched = 1  # set flinched to true


def get_target(opposing_party: Party):
    subheader("Target")

    options = []
    i = 0
    for p in opposing_party:  # print target options
        if p.curr_hp <= 0:  # if the pokemon is dead
            pass
        else:
            option(i, f"{p.name} ({p.id}) | Curr HP: {p.curr_hp}/{p.stats.hp}")
            options.append(i)
        i += 1

    inp = correct_type(input("--> "))

    if inp not in options:
        print(f"ERROR: {inp} was not an option")
        return -1

    return opposing_party[inp]


def weather_check(move: Move, weather: str) -> str:
    if move.weather != "":
        weather = move.weather
    return move.weather if move.weather != "" else weather


def reset_stats(pokemon: SavedPokemon) -> None:
    pokemon.curr_stats.attack = int(pokemon.stats.attack)
    pokemon.curr_stats.defense = int(pokemon.stats.defense)
    pokemon.curr_stats.sp_attack = int(pokemon.stats.sp_attack)
    pokemon.curr_stats.sp_defense = int(pokemon.stats.sp_defense)
    pokemon.curr_stats.speed = int(pokemon.stats.speed)


def health_check(turn_order: list[SavedPokemon], party1_pokemon: Party,
                 party2_pokemon: Party, fainted_pokemon: list[SavedPokemon]) -> int:
    for p in turn_order:
        if p.curr_hp <= 0 and p not in fainted_pokemon:
            print(f"{format_name(p)} has fainted!")
            fainted_pokemon.append(p)  # add to list of fainted pokemon

    if all(p.curr_hp <= 0 for p in party2_pokemon):
        return 1  # 1 won
    elif all(p.curr_hp <= 0 for p in party1_pokemon):
        return 2

    return 0


