from ..Classes.Pokemon import Pokemon
from ..tools import *
import copy


def level_check(p: SavedPokemon, to_next_level, move_levels, moves):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    curr_pokemon = Pokemon.get_pokemon(p.dex_entry)

    if int(p.exp) >= int(
            to_next_level[int(p.level) + 1][curr_pokemon.exp_growth]):  # if exp is good to level up
        level_up(p, to_next_level, moves, True, True)  # level up the pokemon
        level_check(p, to_next_level, move_levels, moves)  # recursive call in case double level up
    evolution_check(p, to_next_level, moves)


def level_up(pokemon: SavedPokemon, to_next_level, moves, announce, sub_exp):
    # pokemon = the pokemon to level up
    # p = stored info about pokemon

    # try: # ensure that pokemon is the actual pokemon itself, not the full list of all pokemon
    #    name = pokemon['Name']
    # except Exception:
    #    pokemon = pokemon[p['Pid']]

    if sub_exp:
        pokemon.exp -= to_next_level[pokemon.level + 1][pokemon['Exp Growth']]  # subtract needed exp from pokemon exp

    old = copy.deepcopy(pokemon)

    pokemon.level += 1  # increase level
    pokemon.stats.hp = int((int(pokemon.ivs.hp) + 2 * int(pokemon.stats.hp) + (int(pokemon.evs.hp) / 4))
                           * int(pokemon.level) / 100) + 10 + int(
        pokemon.level)
    # ( (IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 10 + Level

    # (((IV + 2 * BaseStat + (EV/4) ) * Level/100 ) + 5) * Nature Value
    pokemon.stats.hp = int(0.001 * (2 * pokemon.base_stats.hp + pokemon.ivs.hp + (0.25 * pokemon.evs.hp)
                                    * pokemon.level) + pokemon.level + 10)

    stat_list = ["attack", "defense", "sp_attack", "sp_defense", "speed"]  # make list of stats
    for s in stat_list:  # set each stat
        # I should never be allowed to write code again
        setattr(pokemon.stats, s, int(.001 * (2 * getattr(pokemon.base_stats, s) + getattr(pokemon.ivs, s)
                                              + (.25 * getattr(pokemon.evs, s))) * pokemon.level + 5))

    # stat info: https://pokemon.fandom.com/wiki/Statistics

    if announce is True:
        print(pokemon.full_name, "leveled up to level", pokemon.level)  # notify user
        print_stat_changes(pokemon, old)

    learn_moves(pokemon, to_next_level, moves)  # learn moves if any


def print_stat_changes(new_p, old_p, stat_list=None):  # make list of stats
    if stat_list is None:
        stat_list = ["HP", "Attack", "Defense", "Sp Attack", "Sp Defense",
                     "Speed"]
    for stat in stat_list:
        print(stat, ": ", old_p[stat], " --> ", new_p[stat], sep="")
    print("")  # print newline


def learn_moves(p, move_levels, moves):
    try:  # get moves learnable at their curr level
        learnables = move_levels[p.dex_entry][p.level]
    except Exception:  # if there aren't any
        return

    try:  # turn into a list
        curr_moves = p.moves.split(',')
    except Exception:  # if can't turn into a list, take the 1 move and put it in a list
        curr_moves = [p.moves]

    i = 0
    for _ in curr_moves:
        curr_moves[i] = int(curr_moves[i])
        i += 1

    for m in learnables:
        if int(m) not in curr_moves:
            print(p.name, " wants to learn ", moves[int(m)]['Name'], ".", sep="")

            if len(curr_moves) >= 4:
                print("Forget a move to learn ", moves[int(m)]['Name'], "?", sep="")
                option(0, "Yes")
                option(1, "No")
                inp = input("--> ")

                try:
                    inp = int(inp)
                except Exception:
                    print(inp, "was not an option")
                    learn_moves(p, move_levels, moves)  # try again
                    return

                if inp == 0:  # Yes
                    i = 0
                    for c in curr_moves:
                        option(i, moves[int(c)]['Name'])
                        i += 1

                    inp = input("--> ")

                    try:  # try to turn inp into an integer
                        inp = int(inp)
                    except Exception:
                        print(inp, "was not an option")
                        learn_moves(p, move_levels, moves)  # try again
                        return

                    try:  # try to replace move with new move
                        curr_moves[inp] = int(m)
                    except Exception:
                        print(inp, "was not an option")
                        learn_moves(p, move_levels, moves)  # try again
                        return

                    new_moves = ""
                    i = 0
                    for c in curr_moves:  # replace moves
                        new_moves += str(c)
                        if i < 3:
                            new_moves += ","
                        i += 1

                    p.moves = new_moves

                    print(p.name, " has learned ", moves[int(m)]['Name'], ".", sep="")

                elif inp == 1:  # No
                    pass

                else:  # Incorrect input
                    print(inp, "was not an option")
                    learn_moves(p, move_levels, moves)  # try again
                    return

            else:  # length of moves is less than 4
                p.moves = str(p.moves) + "," + str(m)
                print(p.name, " has learned ", moves[int(m)]['Name'], ".", sep="")


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
        print(p['Full Name'], " wants to evolve.")
        option(0, "Allow")
        option(1, "Deny")
        inp = correct_type(input("--> "))

        if inp == 0:
            old_p = copy.deepcopy(p)
            p.pid = Pokemon.get_pokemon(curr_pokemon.next_evo)
            p.pname = Pokemon.get_pokemon(p.pid).name

            p.level -= 1  # delevel
            level_up(p, to_next_level, moves, False, False)  # relevel

            print(p.full_name, " evolved into ", p.pname, "!", sep="")

            # update full name
            if p.tid == "":
                p.full_name = "Wild " + str(p.pname)
            else:
                p.full_name = str(p.tname) + "'s " + str(p.pname) + " (" + str(p.name) + ")"

            print_stat_changes(old_p, p)

        else:
            print(p.full_name, "did not evolve.")
