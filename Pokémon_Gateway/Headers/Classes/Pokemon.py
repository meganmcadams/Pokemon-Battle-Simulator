class Pokemon(object):
    def __init__(self, list):
        self.list = list # is a dictionary with keys as index 0
    def add(self, pid, pokemon):
        self.list[pid] = pokemon
        # add pokemon to master list
    def remove(self, pid):
        del self.list[pid]
        # remove pokemon from master list
    def replace(self, pid, pokemon):
        self.list[pid] = pokemon
        # replace pokemon with new pokemon
    def get_pid(self, name):
        for p in self.list:
            if p['Name'] == name:
                return p['ID']
        return -1
        # find pid (pokemon id) of pokemon “name”
    def get_name(self, pid):
        return self.list[pid]['Name']
        # find name of pokemon “pid”