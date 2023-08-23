import typing

ITEMS: typing.Dict[int, 'Item'] = {}


class Item:

    def __init__(self):
        # ID	Name	Type	Action	Stat	Description	Buy	Sell	Discoverable
        self.id: int = 0
        self.name: str = ""
        self.type: str = ""
        self.action: str = ""
        self.stat: str = ""
        self.description: str = ""
        self.buy: int = 0
        self.sell: int = 0
        self.discoverable: int = 0

    @staticmethod
    def register(item_: dict):
        item = Item()
        item.id = item_["ID"]
        item.name = item_["Name"]
        item.type = item_["Type"]
        item.action = item_["Action"]
        item.stat = item_["Stat"]
        item.description = item_["Description"]
        item.buy = item_["Buy"]
        item.sell = item_["Sell"]
        item.discoverable = item_["Discoverable"]

        ITEMS[item.id] = item

    @staticmethod
    def as_dicts():
        retval = {}
        for key, value in ITEMS.items():
            retval[key] = {
                "ID": value.id,
                "Name": value.name,
                "Type": value.type,
                "Action": value.action,
                "Stat": value.stat,
                "Description": value.description,
                "Buy": value.buy,
                "Sell": value.sell,
                "Discoverable": value.discoverable
            }
        return retval

    @staticmethod
    def get_item(id_: int) -> 'Item':
        return ITEMS[id_]

    @staticmethod
    def get_all() -> dict[int, 'Item']:
        return ITEMS

    @staticmethod
    def get_category(category: str) -> typing.List['Item']:
        return [item for item in ITEMS.values() if item.type == category]

    @staticmethod
    def categorize() -> typing.Dict[str, typing.List['Item']]:
        retval = {}
        for item in ITEMS.values():
            if item.type not in retval.keys():
                retval[item.type] = []
            retval[item.type].append(item)
        return retval