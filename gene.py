class Gene:
    def __init__(self, geneName, stat, isSuperior):
        self.geneName = geneName
        self.stat = stat
        self.isSuperior = isSuperior

    def mutate(self, randstat):
        self.isSuperior = not self.isSuperior
        self.stat = randstat