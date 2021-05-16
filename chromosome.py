from tokenize import String
from typing import List

from gene import Gene
import random


class Chromosome:
    def __init__(self):
        self.chromosome = list()

    def asList(self):
        return self.chromosome

    def appendGene(self, gene1: Gene, gene2: Gene):
        if gene1.geneName == gene2.geneName:
            self.chromosome.append((gene1, gene2))

    def getHalfChromosomeAsList(self):
        self.sortChromosome()
        result = list()
        for i in range(len(self.chromosome)):
            rand = random.random()
            if rand < 0.5:
                result.append(self.chromosome[i][0])
            else:
                result.append(self.chromosome[i][1])
        return result

    def getPhenotypesAsList(self) -> List[tuple]:
        self.sortChromosome()
        result = list()
        for i in range(len(self.chromosome)):
            superiorGene = self.chromosome[i][0] if self.chromosome[i][0].stat > self.chromosome[i][1].stat else self.chromosome[i][1]
            result.append((superiorGene.geneName, superiorGene.stat))
        return result


    def sortChromosome(self):
        self.chromosome.sort(key=lambda x: x[0].geneName)