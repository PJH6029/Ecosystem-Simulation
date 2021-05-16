from chromosome import Chromosome
from creature import Creature
from ecosystem import Ecosystem
import random
from constant import Constant as c
from gene import Gene
import numpy as np
from matplotlib import pyplot as plt

def simulate2(i):
    genList = ['power', 'velocity', 'intelligence', 'fertility', 'hostility']
    numLives = 30

    print(f"init start. numlives: {numLives}")
    ecosystem = Ecosystem(numLives=numLives, genList=genList, MAP_WIDTH=c.MAP_WIDTH, MAP_HEIGHT=c.MAP_HEIGHT)
    print(f"init finished: {i}-----------------------------------------")

    data = list()
    powerData = list()
    veloData = list()
    intelData = list()
    fertilData = list()
    hostilData = list()
    numLivesData = list()

    epochtime = 500

    while ecosystem.time < epochtime:
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

        avgDict = {'power': 0,
                   'velocity': 0,
                   'intelligence': 0,
                   'fertility': 0,
                   'hostility': 0, }
        if not ecosystem.numLives:
            data.append((0, avgDict))
            print("numLives is 0")
            continue
        if ecosystem.numLives < 0:
            # data.append((0, avgDict))
            print("numLives < 0")
            continue

        for creature in ecosystem.lives:
            infos = creature.getInfo()
            for geneName in avgDict.keys():
                avgDict[geneName] += infos[geneName]
        for geneName in avgDict.keys():
            avgDict[geneName] /= ecosystem.numLives
        data.append((ecosystem.numLives, avgDict))
    print(f"simulation finished: {i}---------------------------------------")

    for numLives, d in data:
        powerData.append(d['power'])
        veloData.append(d['velocity'])
        intelData.append(d['intelligence'])
        fertilData.append(d['fertility'])
        hostilData.append(d['hostility'])
        numLivesData.append(numLives)

    f, axes = plt.subplots(2, 3)
    xrange = np.arange(epochtime)
    axes[0][0].set_title("power")
    axes[0][0].plot(xrange, powerData)

    axes[0][1].set_title("velocity")
    axes[0][1].plot(xrange, veloData)

    axes[0][2].set_title("intelligence")
    axes[0][2].plot(xrange, intelData)

    axes[1][0].set_title("fertility")
    axes[1][0].plot(xrange, fertilData)

    axes[1][1].set_title("hostility")
    axes[1][1].plot(xrange, hostilData)

    axes[1][2].set_title("numLives")
    axes[1][2].plot(xrange, numLivesData)

    plt.show()

    return ecosystem.numLives, ecosystem.lives