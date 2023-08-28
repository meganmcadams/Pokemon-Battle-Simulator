import dataclasses
import typing
from typing import Union


# TODO: move to dict
POKEMON: dict[int, 'Pokemon'] = {}


class Pokemon:
    def __init__(self, ):
        self.dex_entry: int = 0
        self.name: str = ""
        self.evo: str = ""
        self.base_evo: str = ""
        self.next_evo: str = ""
        self.evolve_level: int = 0
        self.learnable_moves = []
        self.type_effectiveness: typing.Dict[str, float] = {}
        self.base_egg_steps: int = 0
        self.capture_rate: float = 0
        self.classification: str = ""
        self.exp_growth: str = ""
        self.height: float = 0
        self.gender_ratio: float = 0
        self.base_total: int = 0
        self.exp_yield: int = 0
        self.evs_given: EVs = None
        self.total_evs: int = 0
        self.base_stats: Stats = None
        self.types: typing.List[str] = []
        self.weight: float = 0
        self.gen: int = 0
        self.legendary: int = 0

    # def __dict__(self):

    def to_dict(self) -> dict:
        return {
                'dex_entry': self.dex_entry,
                'name': self.name,
                'evo': self.evo,
                'base_evo': self.base_evo,
                'next_evo': self.next_evo,
                'evolve_level': self.evolve_level,
                'learnable_moves': self.learnable_moves,
                'type_effectiveness': self.type_effectiveness,
                'base_egg_steps': self.base_egg_steps,
                'capture_rate': self.capture_rate,
                'classification': self.classification,
                'exp_growth': self.exp_growth,
                'height': self.height,
                'gender_ratio': self.gender_ratio,
                'base_total': self.base_total,
                'exp_yield': self.exp_yield,
                'evs_given': self.evs_given,
                'total_evs': self.total_evs,
                'base_stats': self.base_stats,
                'types': self.types,
                'weight': self.weight,
                'gen': self.gen,
                'legendary': self.legendary
            }

    def __str__(self):
        return f"Pokemon: {self.name}\n" \
                f"ID: {self.dex_entry}\n" \
                f"Evolution: {self.evo}\n" \
                f"Base Evolution: {self.base_evo}\n" \
                f"Next Evolution: {self.next_evo}\n" \
                f"Evolves at Level: {self.evolve_level}\n" \
                f"Learnable Moves: {self.learnable_moves}\n" \
                f"Type Effectiveness: {self.type_effectiveness}\n" \
                f"Base Egg Steps: {self.base_egg_steps}\n" \
                f"Capture Rate: {self.capture_rate}\n" \
                f"Classification: {self.classification}\n" \
                f"EXP Growth: {self.exp_growth}\n" \
                f"Height: {self.height}\n" \
                f"Gender Ratio: {self.gender_ratio}\n" \
                f"Base Total: {self.base_total}\n" \
                f"EXP Yield: {self.exp_yield}\n" \
                f"EVs: {self.evs_given}\n" \
                f"Total EVs: {self.total_evs}\n" \
                f"Stats: {self.base_stats}\n" \
                f"Types: {self.types}\n" \
                f"Weight: {self.weight}\n" \
                f"Generation: {self.gen}\n" \
                f"Legendary: {self.legendary}\n"

    @staticmethod
    def iter() -> 'Pokemon':
        for key, item in POKEMON.items():
            yield item

    @staticmethod
    def create_pokemon(dict_: dict) -> 'Pokemon':
        pokemon_types = [
            'Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying',
            'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock',
            'Steel', 'Water'
        ]
        pokemon_stats = [
            'HP', 'Attack', 'Defense', 'Sp Attack', 'Sp Defense', 'Speed'
        ]

        mon = Pokemon()
        mon.dex_entry = dict_['ID']
        mon.name = dict_['Name']
        mon.evo = dict_['Evo']
        mon.base_evo = dict_['Base Evo']
        mon.next_evo = dict_['Next Evo']
        mon.evolve_level = dict_['Evolves at Level']
        mon.learnable_moves = dict_['Learnable Moves']
        mon.base_egg_steps = dict_['Base Egg Steps']
        mon.capture_rate = dict_['Capture Rate']
        mon.classification = dict_['Classification']
        mon.exp_growth = dict_['Exp Growth']
        mon.height = dict_['Height']
        mon.gender_ratio = dict_['Percent Male']
        mon.base_total = dict_['Base Total']
        mon.exp_yield = dict_['Exp']
        mon.total_evs = dict_['Total EVs']
        mon.types = [dict_['Type1'], dict_['Type2']]
        mon.weight = dict_['Weight']
        mon.gen = dict_['Gen']
        mon.legendary = dict_['Legendary']
        mon.base_stats = Stats()
        mon.evs_given = EVs()
        for i in pokemon_types:
            mon.type_effectiveness[i] = dict_[i]
        for i in pokemon_stats:
            internal_name = i.lower().replace(" ", "_")
            if i is not None:
                setattr(mon.evs_given, internal_name, dict_[i + " EV"])
            setattr(mon.base_stats, internal_name, dict_[i])

        return mon

    @staticmethod
    def get_pokemon(id_: Union[int, str]) -> typing.Union['Pokemon', int]:
        if isinstance(id_, int):
            return POKEMON[id_]
        for key, value in POKEMON.items():
            if value.name == id_:
                return value
        return -1

    @staticmethod
    def register(pokemon: dict):
        mon = Pokemon.create_pokemon(pokemon)
        POKEMON[mon.dex_entry] = mon

    @staticmethod
    def get_level_exp(exp_growth: str, level: int) -> int:
        if exp_growth == "Fast":
            return int((4 * (level ** 3)) / 5)
        if exp_growth == "Medium Fast":
            return int(level ** 3)
        if exp_growth == "Medium Slow":
            return int((6 / 5 * (level ** 3)) - (15 * (level ** 2)) + (100 * level) - 140)
        if exp_growth == "Slow":
            return int((5 * (level ** 3)) / 4)
        if exp_growth == "Erratic":
            if level < 50:
                return int(((level ** 3) * (100 - level)) / 50)
            if 50 <= level < 68:
                return int(((level ** 3) * (150 - level)) / 100)
            if 68 <= level <= 98:
                return int(((level ** 3) * ((1911 - (10 * level)) / 3)) / 500)
            return int(((level ** 3) * (160 - level)) / 100)
        if exp_growth == "Fluctuating":
            if level < 15:
                return int((level ** 3) * ((((level + 1) / 3) + 24) / 50))
            if 15 <= level < 36:
                return int((level ** 3) * (level + 14) / 50)
            return int((level ** 3) * (((level / 2) + 32) / 50))

    @staticmethod
    def get_all() -> typing.Dict[int, 'Pokemon']:
        return POKEMON


@dataclasses.dataclass
class Stats:
    hp: int = 0
    attack: int = 0
    defense: int = 0
    sp_attack: int = 0
    sp_defense: int = 0
    speed: int = 0


EVs = Stats
IVs = Stats
