import typing

from Headers import SavedPokemon

PARTIES = {}


class Party:
    def __init__(self, id_: int = 0, name: str = "", pokemon: typing.List[SavedPokemon] = None):
        self.id: int = id_
        self.name: str = name
        self.pokemon: typing.List[SavedPokemon] = [] if pokemon is None else pokemon

    @staticmethod
    def get_party(id_: int) -> typing.Union['Party', typing.Literal[-1]]:
        return PARTIES.get(id_, -1)
        # for party in PARTIES:
        #     if party.id == id_:
        #         return party
        # return -1

    @staticmethod
    def get_all() -> typing.Dict[int, 'Party']:
        return PARTIES

    @staticmethod
    def register(party_: typing.Union['Party', dict]) -> None:
        if isinstance(party_, Party):
            PARTIES[party_.id] = party_
        else:
            party = Party()
            party.id = party_["ID"]
            party.name = party_["Name"]
            party.pokemon = [SavedPokemon.get_pokemon(int(i)) for i in str(party_["Pokemon"]).rstrip(',').split(',')]
            PARTIES[party.id] = party

    @staticmethod
    def delete(id_: int) -> None:
        del PARTIES[id_]

    @staticmethod
    def as_dicts() -> typing.Dict[int, dict]:
        retval = {}
        for key, value in PARTIES.items():
            retval[key] = {
                "ID": value.id,
                "Name": value.name,
                "Pokemon": ','.join([str(pokemon.id) for pokemon in value.pokemon])
            }
        return retval

    def __iter__(self):
        return self.pokemon.__iter__()

    def __setitem__(self, key, value):
        self.pokemon[key] = value

    def __getitem__(self, item):
        return self.pokemon[item]

    @staticmethod
    def list_parties():
        print(f"{'ID':<5}{'Name':<20}")
        for key, value in PARTIES.items():
            print(f"{key:<5}{value.name:<20}")
