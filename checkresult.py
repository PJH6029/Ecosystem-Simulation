import simulate
from matplotlib import pyplot as plt
import numpy as np


# epoch = 5

f, axes = plt.subplots(2, 3)
def main(epoch):
    data = list()
    powerData = list()
    veloData = list()
    intelData = list()
    fertilData = list()
    hostilData = list()
    numLivesData = list()

    for i in range(epoch):
        numLives, result = simulate.simulate(i)
        print(f"result of epoch {i}: {numLives}")
        avgDict = {'power': 0,
                  'velocity': 0,
                  'intelligence': 0,
                  'fertility': 0,
                  'hostility': 0,}
        if not numLives:
            data.append((0, avgDict))
            print("numLives is 0")
            continue
        if numLives < 0:
            # data.append((0, avgDict))
            print("numLives < 0")
            continue
          
        for creature in result:
            infos = creature.getInfo()
            for geneName in avgDict.keys():
                avgDict[geneName] += infos[geneName]
        for geneName in avgDict.keys():
            avgDict[geneName] /= numLives
        data.append((numLives, avgDict))

    for numLives, d in data:
        powerData.append(d['power'])
        veloData.append(d['velocity'])
        intelData.append(d['intelligence'])
        fertilData.append(d['fertility'])
        hostilData.append(d['hostility'])
        numLivesData.append(numLives)


    xrange = np.arange(epoch)
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
