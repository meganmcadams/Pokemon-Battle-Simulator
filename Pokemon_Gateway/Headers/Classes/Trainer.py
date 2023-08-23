from Headers.Classes.Pokemon import Pokemon
from Headers.Classes.SavedPokemon import SavedPokemon

TRAINERS = {}


class Trainer:
    def __init__(self):
        self.id: int = 0
        self.player: str = ""
        self.name: str = ""
        self.pokedex_count: list[Pokemon] = []
        self.pokedex: str = ""
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
        TRAINERS[trainer.id] = trainer

    @staticmethod
    def get_trainer(id_: int) -> 'Trainer':
        return TRAINERS[id_]