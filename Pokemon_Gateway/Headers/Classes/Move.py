import random

MOVES = {}


class Move:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.type = ""
        self.category = ""
        self.pp = 0
        self.power = 0
        self.accuracy = 0.0
        self.status_chance = 0.0
        self.status = ""
        self.times = (0, 0)
        self.weather = 0
        self.p_critical_hits = 0
        self.p_hp = 0
        self.p_attack = 0
        self.p_defense = 0
        self.p_sp_attack = 0
        self.p_sp_defense = 0
        self.p_speed = 0
        self.o_hp = 0
        self.o_attack = 0
        self.o_defense = 0
        self.o_sp_attack = 0
        self.o_sp_defense = 0
        self.o_speed = 0
        self.flinch = False
        self.description = ""

    def __getitem__(self, item):
        item = item.lower().replace(" ", "_")
        return self.__getattribute__(item)

    @staticmethod
    def register(move: dict) -> None:
        to_add = Move()
        for key, value in move.items():
            setattr(to_add, key.lower().replace(" ", "_"), value)
        stats = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]
        for stat in stats:
            if getattr(to_add, f"p_{stat}") == '':
                setattr(to_add, f"p_{stat}", 0)
            if getattr(to_add, f"o_{stat}") == '':
                setattr(to_add, f"o_{stat}", 0)

        MOVES[to_add.id] = to_add

    @staticmethod
    def get_move(index: int) -> 'Move':
        return MOVES[index]

    @staticmethod
    def get_all() -> dict[int, 'Move']:
        return MOVES

    @staticmethod
    def random() -> 'Move':
        return random.choice(MOVES)
