class Container(object):
    def __init__(self, list):
        self.list = list # is a dictionary with keys as index 0

    def add(self, id, item):
        self.list[id] = item
        # add pokemon to master list

    def remove(self, id):
        del self.list[id]
        # remove pokemon from master list

    def replace(self, id, item):
        self.list[id] = item
        # replace item with new item

    def get_id(self, field_name, field_content):
        for item in self.list:
            if item[field_name] == field_content:
                return item['ID']
        return -1
        # find id of item with field (field_name) matching field_content

    def get_field_content(self, id, field_content):
        return self.list[id][field_content]
        # find name of item's "field_name"