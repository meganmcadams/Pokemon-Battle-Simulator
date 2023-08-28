import typing

from Headers import Pokemon, Item
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
    def register(trainer_: typing.Union[dict, 'Trainer']) -> None:
        if isinstance(trainer_, Trainer):
            TRAINERS[trainer_.id] = trainer_
            return
        # todo: finish
        trainer = Trainer()
        trainer.id = trainer_["ID"]
        trainer.player = trainer_["Player"]
        trainer.name = trainer_["Name"]
        if trainer_["Pokedex"]:
            trainer.pokedex = [Pokemon.get_pokemon(int(i)) for i in str(trainer_["Pokedex"]).rstrip(',').split(',')]
        trainer.pokedex_count = trainer_["Pokedex Count"]
        trainer.pokemon_count = trainer_["Pokemon Count"]
        # todo: trainer["Pokemon"] is a list of dex entries, not SavedPokemon entries
        if trainer_["Pokemon"]:
            trainer.pokemon = [Pokemon.get_pokemon(int(i)) for i in str(trainer_["Pokemon"]).rstrip(',').split(',')]
            # trainer.pokemon = [SavedPokemon.get_pokemon(int(i)) for i in str(trainer_["Pokemon"]).rstrip(',').split(',')]
        trainer.money = trainer_["Money"]
        if trainer_["Items"]:
            trainer.items = [Item.get_item(int(i)) for i in str(trainer_["Items"]).rstrip(',').split(',')]
        TRAINERS[trainer.id] = trainer

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
                "Pokedex": ','.join([str(i.id) for i in value.pokedex]),
                "Pokemon Count": value.pokemon_count,
                "Pokemon": ','.join([str(i.id) for i in value.pokemon]),
                "Money": value.money,
                "Items": ','.join([str(i.id) for i in value.items])
            }
        return retval

    @staticmethod
    def delete(id_: int) -> None:
        del TRAINERS[id_]

    @staticmethod
    def list_trainers() -> None:
        name_width = max([len(value.name) for value in TRAINERS.values()]) + 2
        print(f"{'ID':<5}{'Name':<{name_width}}{'Player':<20}")
        for key, value in TRAINERS.items():
            print(f"{key:<5}{value.name:<{name_width}}{value.player:<20}")