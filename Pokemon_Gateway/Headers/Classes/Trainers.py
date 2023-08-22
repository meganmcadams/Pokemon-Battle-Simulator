from Headers.Classes import Container

TRAINERS = {}


class Trainers(Container.Container):
    def __init__(self, list_):
        super().__init__(list_)

    @staticmethod
    def get_all():
        return TRAINERS