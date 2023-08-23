import copy
import typing

from Headers import Move
from Headers import Pokemon
from Headers import SavedPokemon
from Headers.tools import option, correct_type


def level_check(pokemon: SavedPokemon, move_levels):
    # if exp is good to level up
    if (int(pokemon.exp) >= int(pokemon.get_level_exp(pokemon.exp_growth, pokemon.level + 1)) -
            int(pokemon.get_level_exp(pokemon.exp_growth, pokemon.level))):
        level_up(pokemon, move_levels, True, True)  # level up the pokemon
        level_check(pokemon, move_levels)  # recursive call in case double level up
    evolution_check(pokemon, move_levels)


def level_up(pokemon: SavedPokemon, move_levels, announce: bool, sub_exp: bool):

    if sub_exp:
        # i dont know how this works, but it does
        pokemon.exp -= Pokemon.get_level_exp(pokemon.exp_growth, pokemon.level + 1) - Pokemon.get_level_exp(
            pokemon.exp_growth, pokemon.level)

    old = copy.deepcopy(pokemon)

    pokemon.level += 1  # increase level
    # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level

    # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
    pokemon.stats.hp = int(0.001 * (2 * pokemon.base_stats.hp + pokemon.ivs.hp + (0.25 * pokemon.evs.hp)
                                    * pokemon.level) + pokemon.level + 10)
    # check for shedinja
    if pokemon.dex_entry == 292:
        pokemon.stats.hp = 1

    stat_list = ["attack", "defense", "sp_attack", "sp_defense", "speed"]  # make list of stats
    for s in stat_list:  # set each stat
        # I should never be allowed to write code again
        setattr(pokemon.stats, s, int(.001 * (2 * getattr(pokemon.base_stats, s) + getattr(pokemon.ivs, s)
                                              + (.25 * getattr(pokemon.evs, s))) * pokemon.level + 5))

    # stat info: https://pokemon.fandom.com/wiki/Statistics

    if announce is True:
        print(pokemon.full_name, "leveled up to level", pokemon.level)  # notify user
        print_stat_changes(pokemon, old)

    learn_moves(pokemon, move_levels)  # learn moves if any


def print_stat_changes(new_p: SavedPokemon, old_p: SavedPokemon, stat_list=None):  # make list of stats
    if stat_list is None:
        stat_list = ["HP", "Attack", "Defense", "Sp Attack", "Sp Defense",
                     "Speed"]
    for stat in stat_list:
        # could do this with getattr, but I'm too lazy to change it.
        print(f"{stat}: {old_p[stat]} --> {new_p[stat]}")
    print("")  # print newline


def learn_moves(p: SavedPokemon, move_levels: dict[int, dict[int, list[int]]]):
    try:  # get moves learnable at their curr level
        learnables = move_levels[p.dex_entry][p.level]
    except Exception:  # if there aren't any
        return

    curr_moves = p.moves

    for m in learnables:
        if int(m) not in curr_moves:
            print(f"{p.name} wants to learn {Move.get_move(int(m)).name}.")

            if len(curr_moves) >= 4:
                print(f"Forget a move to learn {Move.get_move(int(m)).name}?")
                option(0, "Yes")
                option(1, "No")
                inp = input("--> ")

                try:
                    inp = int(inp)
                except Exception:
                    print(inp, "was not an option")
                    learn_moves(p, move_levels)  # try again
                    return

                if inp == 0:  # Yes
                    i = 0
                    for c in curr_moves:
                        option(i, Move.get_move(int(c)).name)
                        i += 1

                    inp = input("--> ")

                    try:  # try to turn inp into an integer
                        inp = int(inp)
                    except Exception:
                        print(inp, "was not an option")
                        learn_moves(p, move_levels)  # try again
                        return

                    try:  # try to replace move with new move
                        curr_moves[inp] = Move.get_move(inp)
                    except Exception:
                        print(inp, "was not an option")
                        learn_moves(p, move_levels)  # try again
                        return

                    new_moves = ""
                    i = 0
                    for c in curr_moves:  # replace moves
                        new_moves += str(c)
                        if i < 3:
                            new_moves += ","
                        i += 1

                    p.moves = new_moves

                    print(f"{p.name} has learned {Move.get_move(int(m)).name}.")

                elif inp == 1:  # No
                    pass

                else:  # Incorrect input
                    print(inp, "was not an option")
                    learn_moves(p, move_levels)  # try again
                    return

            else:  # length of moves is less than 4
                p.moves = str(p.moves) + "," + str(m)
                print(f"{p.name} has learned {Move.get_move(int(m)).name}.")


def exp(winning_party: typing.List[SavedPokemon], defeated_party: typing.List[SavedPokemon]):
    print("")  # print newline

    # get exp
    total = 0
    for d in defeated_party:
        total += Pokemon.get_pokemon(d.dex_entry).exp_yield * d.level / 2
    total /= len(defeated_party)  # get average

    for mon in winning_party:
        mon.exp += total
        print(mon.name, "gained", total, "experience points.")

    print("")  # print newline


def evolution_check(p: SavedPokemon, to_next_level, moves):
    curr_pokemon = Pokemon.get_pokemon(p.dex_entry)

    try:
        evolves_at_level = int(curr_pokemon.evolve_level)
    except Exception:
        return  # needs a stone or can't evolve

    if p.level >= evolves_at_level:  # if should evolve
        print(p.full_name, " wants to evolve.")
        option(0, "Allow")
        option(1, "Deny")
        inp = correct_type(input("--> "))

        if inp == 0:
            old_p = copy.deepcopy(p)
            p.pid = Pokemon.get_pokemon(curr_pokemon.next_evo)
            p.pname = Pokemon.get_pokemon(p.pid).name

            p.level -= 1  # delevel
            level_up(p, to_next_level, False, False)  # relevel

            print(f"{pokemon.full_name} evolved into {pokemon.name}!")

            # update full name
            if pokemon.tid == -1:
                pokemon.full_name = f"Wild {pokemon.name}"
            else:
                pokemon.full_name = f"{pokemon.tname}'s {pokemon.name} ({pokemon.nickname})"

            print_stat_changes(old_p, p)

        else:
            print(p.full_name, "did not evolve.")
