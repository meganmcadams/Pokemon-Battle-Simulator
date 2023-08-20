import dataclasses
import typing
from typing import Union

POKEMON: typing.List['Pokemon'] = []


class Pokemon:
    amount = 0

    def __init__(self, dex_entry=0, name="", evo="", base_evo="", next_evo="", evolves_at_level=0,
                 learnable_moves=None, type_effectiveness=None, base_egg_steps=0, capture_rate=0,
                 classification="", exp_growth="", height=0.0, gender_ratio=0.0, base_total=0, exp_yield=0,
                 evs=None, total_evs=0, stats=None, types=None, weight=0.0, gen=0, legendary=False):
        if type_effectiveness is None:
            type_effectiveness = {}
        if learnable_moves is None:
            learnable_moves = []
        if evs is None:
            evs = {}
        if stats is None:
            stats = {}
        if types is None:
            types = []
        self.dex_entry: int = dex_entry
        self.name: str = name
        self.evo: str = evo
        self.base_evo: str = base_evo
        self.next_evo: str = next_evo
        self.evolve_level: int = evolves_at_level
        self.learnable_moves = learnable_moves
        self.type_effectiveness: typing.Dict[str, float] = type_effectiveness
        self.base_egg_steps: int = base_egg_steps
        self.capture_rate: float = capture_rate
        self.classification: str = classification
        self.exp_growth: str = exp_growth
        self.height: float = height
        self.gender_ratio: float = gender_ratio
        self.base_total: int = base_total
        self.exp_yield: int = exp_yield
        self.evs_given: EVs = evs
        self.total_evs: int = total_evs
        self.base_stats: Stats = stats
        self.types: typing.List[str] = types
        self.weight: float = weight
        self.gen: int = gen
        self.legendary: int = legendary

    def __dict__(self):
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

    def __getitem__(self, item):
        # print(self.__dict__())
        try:
            return self.__dict__()[item]
        except KeyError:
            # print(self['stats'])
            header_dict = {
                'ID': self['id'], 'Name': self['name'], 'Evo': self['evo'], 'Base Evo': self['base_evo'],
                'Next Evo': self['next_evo'], 'Evolves at Level': self['evolve_level'],
                'Learnable Moves': self['learnable_moves'], 'Bug': self['type_effectiveness']['Bug'],
                'Dark': self['type_effectiveness']['Dark'], 'Dragon': self['type_effectiveness']['Dragon'],
                'Electric': self['type_effectiveness']['Electric'], 'Fairy': self['type_effectiveness']['Fairy'],
                'Fighting': self['type_effectiveness']['Fighting'], 'Fire': self['type_effectiveness']['Fire'],
                'Flying': self['type_effectiveness']['Flying'], 'Ghost': self['type_effectiveness']['Ghost'],
                'Grass': self['type_effectiveness']['Grass'], 'Ground': self['type_effectiveness']['Ground'],
                'Ice': self['type_effectiveness']['Ice'], 'Normal': self['type_effectiveness']['Normal'],
                'Poison': self['type_effectiveness']['Poison'], 'Psychic': self['type_effectiveness']['Psychic'],
                'Rock': self['type_effectiveness']['Rock'], 'Steel': self['type_effectiveness']['Steel'],
                'Water': self['type_effectiveness']['Water'], 'Base Egg Steps': self['base_egg_steps'],
                'Capture Rate': self['capture_rate'], 'Classification': self['classification'],
                'Exp Growth': self['exp_growth'], 'Height': self['height'], 'Percent Male': self['gender_ratio'],
                'Base Total': self['base_total'], 'EXP': self["Exp"], 'HP EV': self['evs']["HP"],
                'Attack EV': self['evs']["Attack"], 'Defense EV': self['evs']["Defense"],
                'Sp Attack EV': self['evs']["Sp Attack"], 'Sp Defense EV': self['evs']["Sp Defense"],
                'Speed EV': self['evs']["Speed"], 'Total EVs': self['total_evs'],
                'Attack': self['base_stats']["Attack"], 'Defense': self['base_stats']["Defense"],
                'HP': self['base_stats']["HP"], 'Sp Attack': self['base_stats']["Sp Attack"],
                'Sp Defense': self['base_stats']["Sp Defense"], 'Speed': self['base_stats']["Speed"],
                'Type1': self['type1'], 'Type2': self['type2'], 'Weight': self['weight'], 'Gen': self['gen'],
                'Legendary': self['legendary']
            }
            return header_dict[item]

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
        for i in POKEMON:
            yield i

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
            return POKEMON[id_ - 1]
        for mon in POKEMON:
            if mon.name == id_:
                return mon
        return -1

    @staticmethod
    def get_all() -> typing.List['Pokemon']:
        return POKEMON

    @staticmethod
    def register(pokemon: dict):
        POKEMON.append(Pokemon.create_pokemon(pokemon))
        Pokemon.amount += 1

    @staticmethod
    def get_level_exp(exp_growth: str, level: int) -> int:
        if exp_growth == "Fast":
            return (4 * (level ** 3)) / 5
        if exp_growth == "Medium Fast":
            return level ** 3
        if exp_growth == "Medium Slow":
            return (6 / 5 * (level ** 3)) - (15 * (level ** 2)) + (100 * level) - 140
        if exp_growth == "Slow":
            return (5 * (level ** 3)) / 4
        if exp_growth == "Erratic":
            if level < 50:
                return ((level ** 3) * (100 - level)) / 50
            if 50 <= level < 68:
                return ((level ** 3) * (150 - level)) / 100
            if 68 <= level <= 98:
                return ((level ** 3) * ((1911 - (10 * level)) / 3)) / 500
            return ((level ** 3) * (160 - level)) / 100
        if exp_growth == "Fluctuating":
            if level < 15:
                return (level ** 3) * ((((level + 1) / 3) + 24) / 50)
            if 15 <= level < 36:
                return (level ** 3) * (level + 14) / 50
            return (level ** 3) * (((level / 2) + 32) / 50)


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
