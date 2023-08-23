import typing

from Headers import Move
from Headers import Pokemon, IVs, EVs, Stats

SAVED_MONS: typing.Dict[int, 'SavedPokemon'] = {}


class SavedPokemon(Pokemon):
    def __init__(self, dex_entry: int = 0):
        super().__init__()
        self.full_name = ""
        self.id: int = -1
        self.tid = -1
        self.tname = ""
        self.plname = ""
        self.gender = ""
        self.nickname = ""
        self.level = -1
        self.moves: typing.List[Move] = []
        self.battles = -1
        self.status = ""
        self.stats: Stats = Stats()
        self.ivs: IVs = IVs()
        self.evs: EVs = EVs()
        self.curr_stats: Stats = Stats()
        self.exp = 0
        self.flinched = 0

        if dex_entry != 0:
            base_dict = Pokemon.get_pokemon(dex_entry).__dict__()
            for key, item in base_dict.items():
                setattr(self, key, item)

    @staticmethod
    def iter() -> 'SavedPokemon':
        for key, value in SAVED_MONS.items():
            yield value

    @staticmethod
    def register(data: typing.Union[dict, 'SavedPokemon']):
        if isinstance(data, SavedPokemon):
            SAVED_MONS[data.id] = data
        saved_mon = SavedPokemon(data["Pid"])

        saved_mon.id = data['ID']
        saved_mon.tid = data['Tid']
        saved_mon.tname = data['Tname']
        saved_mon.gender = data['Gender']
        saved_mon.nickname = data['Name']
        saved_mon.level = data['Level']

        saved_mon.moves = [Move.get_move(int(i)) or print(i) for i in str(data['Moves']).rstrip(',').split(',')]

        saved_mon.battles = data['Battles']
        saved_mon.status = data['Status']
        saved_mon.curr_stats = Stats()
        saved_mon.ivs = IVs()
        saved_mon.evs = EVs()

        pokemon_stats = [
            'HP', 'Attack', 'Defense', 'Sp Attack', 'Sp Defense', 'Speed'
        ]

        for i in pokemon_stats:
            internal_name = i.lower().replace(" ", "_")
            if i is not None:
                setattr(saved_mon.evs, internal_name, data[i + " EV"])
                setattr(saved_mon.ivs, internal_name, data[i + " IV"])
            setattr(saved_mon.stats, internal_name, data[i])
            setattr(saved_mon.curr_stats, internal_name, data[i])
        saved_mon.curr_stats.hp = data['Curr HP']  # curr hp is defined separately in saved pokemon txt

        SAVED_MONS[saved_mon.id] = saved_mon

    def evolve(self):
        evolution = Pokemon.get_pokemon(self.next_evo)
        self.dex_entry = evolution.dex_entry
        self.name = evolution.name
        self.evo = evolution.evo
        self.base_evo = evolution.base_evo
        self.next_evo = evolution.next_evo
        self.evolve_level = evolution.evolve_level
        self.learnable_moves = evolution.learnable_moves
        self.type_effectiveness = evolution.type_effectiveness
        self.base_egg_steps = evolution.base_egg_steps
        self.capture_rate = evolution.capture_rate
        self.classification = evolution.classification
        self.exp_growth = evolution.exp_growth
        self.height = evolution.height
        self.gender_ratio = evolution.gender_ratio
        self.base_total = evolution.base_total
        self.exp_yield = evolution.exp_yield
        self.evs_given = evolution.evs_given
        self.total_evs = evolution.total_evs
        self.base_stats = evolution.base_stats
        self.types = evolution.types
        self.weight = evolution.weight
        self.gen = evolution.gen
        self.legendary = evolution.legendary

    @staticmethod
    def get_pokemon(id_: typing.Union[int, str]) -> 'SavedPokemon':
        return SAVED_MONS[id_]

    @staticmethod
    def get_all() -> typing.Dict[int, 'SavedPokemon']:
        return SAVED_MONS

    @staticmethod
    def delete(id_: int):
        del SAVED_MONS[id_]
