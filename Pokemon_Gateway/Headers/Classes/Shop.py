from typing import TYPE_CHECKING
from Headers import Item

SHOPS: dict[int, 'Shop'] = {}


class Shop():
    def __init__(self):
        super().__init__()
        self.id: int = 0
        self.name: str = ""
        self.location: str = ""
        self.items: list[Item] = []
        self.berries: int = 0
        self.general_items: int = 0
        self.machine: int = 0
        self.medicine: int = 0
        self.pokeballs: int = 0

    @staticmethod
    def register(shop_: dict) -> None:
        shop = Shop()
        shop.id = shop_["ID"]
        shop.name = shop_["Name"]
        shop.location = shop_["Location"]
        shop.items = [Item.get_item(int(i)) for i in str(shop_["Items"]).rstrip(',').split(',')]
        shop.berries = shop_["Berries"]
        shop.general_items = shop_["General items"]
        shop.machine = shop_["Machine"]
        shop.medicine = shop_["Medicine"]
        shop.pokeballs = shop_["Pokeballs"]
        SHOPS[shop.id] = shop

    @staticmethod
    def as_dicts():
        retval = {}
        for key, value in SHOPS.items():
            retval[key] = {
                "ID": value.id,
                "Name": value.name,
                "Location": value.location,
                "Items": ','.join([str(item.id) for item in value.items]),
                "Berries": value.berries,
                "General items": value.general_items,
                "Machine": value.machine,
                "Medicine": value.medicine,
                "Pokeballs": value.pokeballs
            }
        return retval

    @staticmethod
    def get_shop(id_: int) -> 'Shop':
        return SHOPS[id_]

    @staticmethod
    def get_all() -> dict[int, 'Shop']:
        return SHOPS

    @staticmethod
    def delete(id_: int) -> None:
        del SHOPS[id_]

    @staticmethod
    def list_shops() -> None:
        print(f"{'ID':<5}{'Name':<20}{'Location':<20}")
        for key, value in SHOPS.items():
            print(f"{key:<5}{value.name:<20}{value.location:<20}")