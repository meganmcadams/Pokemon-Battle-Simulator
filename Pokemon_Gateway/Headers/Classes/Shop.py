# from Container import Container

SHOPS = {}


class Shop:
    def __init__(self):
        super().__init__(self)
        self.list = self

    @staticmethod
    def get_all():
        return SHOPS