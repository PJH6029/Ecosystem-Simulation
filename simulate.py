from chromosome import Chromosome
from creature import Creature
from ecosystem import Ecosystem
import random
from constant import Constant as c
from gene import Gene
def simulate(i):
    genList = ['power', 'velocity', 'intelligence', 'fertility', 'hostility']
    numLives = 30

    print(f"init start. numlives: {numLives}")
    ecosystem = Ecosystem(numLives=numLives, genList=genList, MAP_WIDTH=c.MAP_WIDTH, MAP_HEIGHT=c.MAP_HEIGHT)
    print(f"init finished: {i}-----------------------------------------")

    while ecosystem.time < 500:
        ecosystem.nextEpoch()
        # 선택(내부에 evaluation(싸우는거) 포함)
        selectedCreatures = ecosystem.selection(ecosystem.lives)
        # 교차
        crossOveredCreature = ecosystem.crossover(selectedCreatures[0], selectedCreatures[1])
        # 변이
        crossOveredCreature = ecosystem.mutation(crossOveredCreature, c.MUTATION_RATE)
        ecosystem.lives.append(crossOveredCreature)
        ecosystem.created.append(crossOveredCreature)
        ecosystem.time += 1
        ecosystem.numLives += 1
        # print(f'epoch {ecosystem.time}: numLives: {ecosystem.numLives}')
    print(f"simulation finished: {i}---------------------------------------")

    '''
    print(f"numlives: {ecosystem.numLives}")
    print(f"lenoflives: {len(ecosystem.lives)}")
    for cr in ecosystem.lives:
        print(cr)
    '''

    return ecosystem.numLives, ecosystem.lives