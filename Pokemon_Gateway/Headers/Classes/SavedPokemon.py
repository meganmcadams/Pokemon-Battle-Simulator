import typing

from Headers import Move
from Headers import Pokemon, IVs, EVs, Stats

SAVED_MONS: typing.Dict[int, 'SavedPokemon'] = {}


class SavedPokemon(Pokemon):
    def __init__(self, dex_entry: int = 0):
        super().__init__()
        self.full_name = ""
        self.id: int = 0
        self.tid = 0
        self.tname = 0
        self.plname = ""
        self.gender = ""
        self.nickname = ""
        self.level = 0
        self.moves: typing.List[Move] = []
        self.battles = 0
        self.status = ""
        self.curr_hp = 0
        self.stats = Stats()
        self.ivs = IVs()
        self.evs = EVs()
        self.curr_stats = Stats()
        self.exp = 0
        self.flinched = False

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
        saved_mon.curr_hp = data['Curr HP']  # curr hp is defined separately in saved pokemon txt
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

        SAVED_MONS[saved_mon.id] = saved_mon

    @staticmethod
    def get_pokemon(id_: typing.Union[int, str]) -> 'SavedPokemon':
        return SAVED_MONS[id_]

    @staticmethod
    def get_all() -> typing.Dict[int, 'SavedPokemon']:
        return SAVED_MONS
