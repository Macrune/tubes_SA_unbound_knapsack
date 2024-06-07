import time
import tracemalloc

#Function untuk menghiitung total cost dari ite,
def calculateCost(wood, stone, steel):
    rWood = 1
    rStone = 1.5
    rSteel = 2

    return wood*rWood + stone*rStone + steel*rSteel

#Function untuk menghitung total profit berdasarkan rasio yang dimiliki
def calculateProfit(production, population, rProd, rPop):
    return production * rProd + population * rPop

#Function algoritma greedy by weight
def greed_byWeight(weights, values, capacity):
    start_time = time.time()
    tracemalloc.start()

    taken = []
    #Hitung semua cost dari item yang ada dan masukkan pada array
    convWeights = [calculateCost(weights[i][0],weights[i][1], weights[i][2]) for i in range(len(weights))]
    #Sort array cost secara ascending
    #Sort secara ascending untuk mendapat cost min
    sortedW = [calculateCost(weights[i][0],weights[i][1], weights[i][2]) for i in range(len(weights))]
    sortedW.sort()

    curr_capx, curr_capy, curr_capz = capacity
    #Untuk semua item pada array yang telah di sort
    #Loop dari terkecil hingga terbesar
    for i in sortedW:
        #Ambil index asli dari item ke i
        idxmin = convWeights.index(i)
        #Ambil item hingga knapsack tidak cukup
        while curr_capx >= weights[idxmin][0] and curr_capy >= weights[idxmin][1] and curr_capz >= weights[idxmin][2]:
            #Simpan index asli item pada array taken
            taken.append(idxmin)
            curr_capx -= weights[idxmin][0]
            curr_capy -= weights[idxmin][1]
            curr_capz -= weights[idxmin][2]
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(time.time() - start_time)
    #Return hasil greedy
    return taken, (time.time() - start_time)*10**3, peak

#Function greedy by density
def greed_byDensity(weights, values, capacity, ratio):
    start_time = time.time()
    tracemalloc.start()

    taken = []
    #Hitung profit dari setiap item yang ada
    convValues= [calculateProfit(values[i][0], values[i][1], ratio[0], ratio[1]) for i in range(len(values))]
    #Hitung cost dari setiap item yang ada
    convWeights = [calculateCost(weights[i][0],weights[i][1], weights[i][2]) for i in range(len(weights))]
    #Hitung density berdasarkan profit/cost
    convDensity = [convValues[i]/convWeights[i] for i in range(len(weights))]

    #Sort array yang berisi density item secara descending
    #Sort secara descending untuk mendapat density max
    sortedD = [convValues[i]/convWeights[i] for i in range(len(weights))]
    sortedD.sort(reverse=True)

    curr_capx, curr_capy, curr_capz = capacity
    #Untuk semua item pada array yang telah di sort
    #Loop dari density terbesar hingga terkecil
    for i in sortedD:
        #Ambil index asli dari item i
        idxmax = convDensity.index(i)
        #Ambil item hingga knapsack tidak cukup
        while curr_capx >= weights[idxmax][0] and curr_capy >= weights[idxmax][1] and curr_capz >= weights[idxmax][2]:
            #Simpan index asli item pada array
            taken.append(idxmax)
            curr_capx -= weights[idxmax][0]
            curr_capy -= weights[idxmax][1]
            curr_capz -= weights[idxmax][2]
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    #Return hasil barang yang diambil
    return taken, (time.time() - start_time)*10**3, peak

#Function algoritma greedy by profit
def greed_byProfit(weights, values, capacity, ratio):
    start_time = time.time()
    tracemalloc.start()

    taken = []
    #Hitung profit dari setiap item yang ada
    convValues= [calculateProfit(values[i][0], values[i][1], ratio[0], ratio[1]) for i in range(len(values))]
    #Sort array yang berisi profit item secara descending
    #Sort secara descending untuk mendapat profit max
    sortedV = [calculateProfit(values[i][0], values[i][1], ratio[0], ratio[1]) for i in range(len(values))]
    sortedV.sort(reverse=True)
    curr_capx, curr_capy, curr_capz = capacity
    #Untuk semua item pada array yang telah di sort
    #Loop dari profit terbesar hingga terkecil
    for i in sortedV:
        #Ambil index asli dari item i
        idxmax = convValues.index(i)
        #Ambil item hingga knapsack tidak cukup
        while curr_capx >= weights[idxmax][0] and curr_capy >= weights[idxmax][1] and curr_capz >= weights[idxmax][2]:
            #Simpan index asli item pada array
            taken.append(idxmax)
            curr_capx -= weights[idxmax][0]
            curr_capy -= weights[idxmax][1]
            curr_capz -= weights[idxmax][2]
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
     #Return hasil barang yang diambil
    return taken, (time.time() - start_time)*10**3, peak
