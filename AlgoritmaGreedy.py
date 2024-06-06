import time
import tracemalloc

def calculateCost(wood, stone, steel):
    rWood = 1
    rStone = 1.5
    rSteel = 2

    return wood*rWood + stone*rStone + steel*rSteel

def calculateProfit(production, population, rProd, rPop):
    return production * rProd + population * rPop

def greed_byWeight(weights, values, capacity):
    start_time = time.time()
    tracemalloc.start()

    taken = []
    convWeights = [calculateCost(weights[i][0],weights[i][1], weights[i][2]) for i in range(len(weights))]
    sortedW = [calculateCost(weights[i][0],weights[i][1], weights[i][2]) for i in range(len(weights))]
    sortedW.sort()
    curr_capx, curr_capy, curr_capz = capacity
    for i in sortedW:
        idxmin = convWeights.index(i)
        while curr_capx >= weights[idxmin][0] and curr_capy >= weights[idxmin][1] and curr_capz >= weights[idxmin][2]:
            taken.append(idxmin)
            curr_capx -= weights[idxmin][0]
            curr_capy -= weights[idxmin][1]
            curr_capz -= weights[idxmin][2]
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(time.time() - start_time)
    return taken, (time.time() - start_time)*10**3, peak

def greed_byDensity(weights, values, capacity, ratio):
    start_time = time.time()
    tracemalloc.start()
    taken = []
    convValues= [calculateProfit(values[i][0], values[i][1], ratio[0], ratio[1]) for i in range(len(values))]
    convWeights = [calculateCost(weights[i][0],weights[i][1], weights[i][2]) for i in range(len(weights))]
    convDensity = [convValues[i]/convWeights[i] for i in range(len(weights))]
    sortedD = [convValues[i]/convWeights[i] for i in range(len(weights))]
    sortedD.sort(reverse=True)
    curr_capx, curr_capy, curr_capz = capacity
    for i in sortedD:
        idxmax = convDensity.index(i)
        while curr_capx >= weights[idxmax][0] and curr_capy >= weights[idxmax][1] and curr_capz >= weights[idxmax][2]:
            taken.append(idxmax)
            curr_capx -= weights[idxmax][0]
            curr_capy -= weights[idxmax][1]
            curr_capz -= weights[idxmax][2]
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return taken, (time.time() - start_time)*10**3, peak

def greed_byProfit(weights, values, capacity, ratio):
    start_time = time.time()
    tracemalloc.start()

    taken = []
    convValues= [calculateProfit(values[i][0], values[i][1], ratio[0], ratio[1]) for i in range(len(values))]
    sortedV = [calculateProfit(values[i][0], values[i][1], ratio[0], ratio[1]) for i in range(len(values))]
    sortedV.sort(reverse=True)
    curr_capx, curr_capy, curr_capz = capacity
    for i in sortedV:
        idxmax = convValues.index(i)
        while curr_capx >= weights[idxmax][0] and curr_capy >= weights[idxmax][1] and curr_capz >= weights[idxmax][2]:
            taken.append(idxmax)
            curr_capx -= weights[idxmax][0]
            curr_capy -= weights[idxmax][1]
            curr_capz -= weights[idxmax][2]
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return taken, (time.time() - start_time)*10**3, peak
