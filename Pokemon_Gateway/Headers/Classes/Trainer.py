TRAINERS = {}


class Trainer:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return TRAINERS

    @staticmethod
    def register(trainer):
        # todo: finish
        TRAINERS[trainer.id] = trainer
