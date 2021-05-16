from chromosome import Chromosome
from constant import Constant as c

class Creature:
    def __init__(self, x, y, chromosome):
        # power, velocity, intelligence, fertility, hostility, totalEnergy, lifespan
        self.chromosome = chromosome

        self.energyTotal = self.getEnergyTotal()
        self.lifespan = self.getLifeSpan()

        self.x = x
        self.y = y
        '''
        self.power = power
        self.velocity = velocity
        self.intelligence = intelligence
        self.fertility = fertility
        self.hostility = hostility
        self.energy_total = power + velocity + intelligence + fertility # 함수화 필요
        self.energy_left = self.energy_total
        self.lifespan = 100 / self.energy_total # 함수화 필요
        '''

    def age(self, ecosystem):
        self.lifespan -= 1
        if self.lifespan <= 0:
            ecosystem.map_[self.x][self.y] = c.GRASS
            ecosystem.lives.remove(self)
            ecosystem.numLives -= 1

    def getChromosome(self):
        return self.chromosome

    def getHalfChromosomeAsList(self):
        return self.chromosome.getHalfChromosomeAsList()

    def getEnergyTotal(self):
        energyTotal = 0
        for phenotype in self.chromosome.getPhenotypesAsList():
            energyTotal += phenotype[1]  # stat
        return energyTotal

    def getLifeSpan(self):
        if not self.energyTotal:
            return 0
        return 100 / self.energyTotal

    def getInfo(self):
        res = dict()
        chr = self.getChromosome().getPhenotypesAsList()
        for c in chr:
            res[c[0]] = c[1]
        return res

    def __repr__(self):
        s = "Creature: "
        for name, stat in self.getChromosome().getPhenotypesAsList():
            s += (name + ": " + str(stat) + " ")
        return s