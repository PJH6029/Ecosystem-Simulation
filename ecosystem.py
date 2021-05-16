import random
import bisect
from typing import List

from chromosome import Chromosome
from constant import Constant as c

from creature import Creature
from gene import Gene


class Ecosystem:
    '''
    map_ = list()
    time = 0
    lives = list()
    created = list()
    numLives = 0
    '''
    def __init__(self, genList, numLives, MAP_WIDTH, MAP_HEIGHT):
        self.map_ = [[random.randrange(0, 2) for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.numLives = 0
        self.time = 0
        self.lives = list()
        self.created = list()
        for _ in range(numLives):
            x, y = 0, 0
            while True:
                x = random.randrange(0, c.MAP_WIDTH)
                y = random.randrange(0, c.MAP_HEIGHT)
                if self.map_[x][y] != c.OCCUPIED:
                    break
            chromosome = Chromosome()
            for geneName in genList:
                stat = random.randrange(0, 10)
                gene1 = Gene(geneName=geneName, stat=stat, isSuperior=True)
                gene2 = Gene(geneName=geneName, stat=stat, isSuperior=True)
                chromosome.appendGene(gene1, gene2)
            cr = Creature(x, y, chromosome)
            self.numLives += 1
            self.lives.append(cr)
            self.map_[x][y] = c.OCCUPIED

    # 선택 교차 변이 대치
    def selection(self, creatureList: List[Creature]) -> List[Creature]:
        evaluationList: List[int] = list()
        for creature in creatureList:
            evaluationResult: int = Ecosystem.evaluation(creature)
            evaluationList.append(evaluationResult)
        total = sum(evaluationList)
        for i in range(len(evaluationList)):
            evaluationList[i] /= total
        for i in range(1, len(evaluationList)):
            evaluationList[i] += evaluationList[i-1]

        rand1 = random.random()
        rand2 = random.random()
        result1 = bisect.bisect(evaluationList, rand1)
        result2 = bisect.bisect(evaluationList, rand2)

        return [creatureList[result1], creatureList[result2]]

    def crossover(self, creature1: Creature, creature2: Creature) -> Creature:
        # 형질들은 다 똑같이 갖고있어야함
        halfChromosome1 = creature1.getHalfChromosomeAsList()  # random half chromosome
        halfChromosome2 = creature2.getHalfChromosomeAsList()
        resultChromosome = Chromosome()
        for i in range(len(halfChromosome1)):
            gene1 = halfChromosome1[i]
            gene2 = halfChromosome2[i]
            resultChromosome.appendGene(Gene(gene1.geneName, gene1.stat, gene1.isSuperior), Gene(gene2.geneName, gene2.stat, gene2.isSuperior))
        x, y = 0, 0
        while True:
            x = random.randrange(0, c.MAP_WIDTH)
            y = random.randrange(0, c.MAP_HEIGHT)
            if self.map_[x][y] != c.OCCUPIED:
                break
        return Creature(x, y, resultChromosome)

    def mutation(self, creature: Creature, mutationRate: int) -> Creature:
        for genePair in creature.getChromosome().asList():
            geneRand = random.randrange(0, 2)

            mutationRand = random.random()
            if mutationRand < mutationRate:
                statRand = random.randrange(0, 10)
                genePair[geneRand].mutate(statRand)
        return creature
        # reference 확인 필요

    def nextEpoch(self):
        for creature in self.lives:
            creature.age(self)

    @staticmethod
    def evaluation(creature: Creature) -> int: # 대치 역할
        eval = creature.energyTotal - creature.lifespan
        return eval