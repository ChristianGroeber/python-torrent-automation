import os


class EnvParser:
    def __init__(self):
        self.vars = {}

    def get(self, key):
        if key not in self.vars:
            return ''
        return self.vars[key]

    def parse(self, file='.env', load_local=True):
        if not os.path.isfile(file):
            return False
        f = open(file, 'r')
        contents = f.read()
        for line in contents.split('\n'):
            if len(line) > 1 and line[0] != '#':
                split = line.split(' = ')
                self.vars[split[0]] = split[1]
                print(line)
        if load_local:
            self.parse('.env.local', False)
        return True
