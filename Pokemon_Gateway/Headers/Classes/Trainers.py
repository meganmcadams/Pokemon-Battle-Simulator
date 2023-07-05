class Trainers(object):
    def __init__(self, list):
        self.list = list # is a dictionary with keys as index 0
    def add(self, pid, trainer):
        self.list[pid] = trainer
        # add trainer to master list
    def remove(self, pid):
        del self.list[pid]
        # remove trainer from master list
    def replace(self, pid, trainer):
        self.list[pid] = trainer
        # replace trainer with new trainer
    def get_pid(self, name):
        for p in self.list:
            if p['Name'] == name:
                return p['ID']
        return -1
        # find tid (trainer id) of trainer “name”
    def get_name(self, tid):
        return self.list[tid]['Name']
        # find name of trainer “tid”