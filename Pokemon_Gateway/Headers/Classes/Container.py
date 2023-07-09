class Container(dict):
    def __init__(self, dict_):
        super().__init__(dict_)
        self.list = self

    def add(self, pid, trainer):
        self[pid] = trainer
        # add trainer to master list

    def remove(self, pid):
        del self[pid]
        # remove trainer from master list

    def replace(self, pid, trainer):
        self[pid] = trainer
        # replace trainer with new trainer

    def get_pid(self, name):
        return self.get_id('Name', name)

    def get_name(self, tid):
        return self.get_field_content(tid, 'Name')

    def get_id(self, field_name, field_content):
        for item in self:
            if item[field_name] == field_content:
                return item['ID']
        return -1
        # find id of item with field (field_name) matching field_content

    def get_field_content(self, id, field_content):
        return self[id][field_content]
        # find name of item's "field_name"
