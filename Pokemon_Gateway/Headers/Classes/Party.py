import typing

from Headers import SavedPokemon

PARTIES = {}


class Party:
    def __init__(self, id_: int, name: str, pokemon: typing.List[SavedPokemon]):
        self.id: int = id_
        self.name: str = name
        self.pokemon: typing.List[SavedPokemon] = pokemon

    @staticmethod
    def get_party(id_: int) -> typing.Union['Party', typing.Literal[-1]]:
        for party in PARTIES:
            if party.id == id_:
                return party
        return -1

    @staticmethod
    def get_all() -> typing.Dict[int, 'Party']:
        return PARTIES

    @staticmethod
    def register(id_: int, party: 'Party') -> None:
        PARTIES[id_] = party

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