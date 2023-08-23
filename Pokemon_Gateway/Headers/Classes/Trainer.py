import typing

from Headers import Pokemon
from Headers import SavedPokemon

TRAINERS = {}


class Trainer:
    def __init__(self):
        self.id: int = 0
        self.player: str = ""
        self.name: str = ""
        self.pokedex: list[Pokemon] = []
        self.pokedex_count: int = 0
        self.pokemon_count: int = 0
        self.pokemon: list[SavedPokemon] = []
        self.money: int = 0
        self.items: list[str] = []


    @staticmethod
    def get_all():
        return TRAINERS

    @staticmethod
    def register(trainer):
        # todo: finish
        TRAINERS[trainer["ID"]] = trainer

    @staticmethod
    def get_trainer(id_: int) -> 'Trainer':
        return TRAINERS[id_]

    @staticmethod
    def as_dicts() -> typing.Dict[int, dict]:
        retval = {}
        for key, value in TRAINERS.items():
            retval[key] = {
                "ID": value.id,
                "Player": value.player,
                "Name": value.name,
                "Pokedex Count": value.pokedex_count,
                "Pokedex": value.pokedex,
                "Pokemon Count": value.pokemon_count,
                "Pokemon": value.pokemon,
                "Money": value.money,
                "Items": ','.join(value.items)
            }

    @staticmethod
    def delete(id_: int) -> None:
        del TRAINERS[id_]