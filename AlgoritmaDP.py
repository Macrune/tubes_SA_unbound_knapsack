import time
import tracemalloc


def unbounded_knapsack(n, W1, W2, W3, weights, profits):
    """
    Weight = limit atau batas dari knapsack
    Cost = harga jika barang diambil
    Profit = total profit yang diapat jika barang diambil
    """

    start_time = time.time()
    tracemalloc.start()

    #Top-Down
    memo = {}

    #Calculate value pada tabel
    def dp(w1, w2, w3):
        #Return value jika sudah pernah dihitung
        if (w1, w2, w3) in memo:
            return memo[(w1, w2, w3)]
        
        max_profit = 0
        #Buat tabel dynamic programming berdasarkan top-down
        #Looping pada setiap item
        for i in range(n):
            w1_i, w2_i, w3_i = weights[i]
            p1_i, p2_i = profits[i]
            #JIka cost lebih kecil dari total weight maka
            if w1 >= w1_i and w2 >= w2_i and w3 >= w3_i:
                #Hitung profit secara recursive
                #Rumus profit saat barang ke i diambil
                #Rumus profit p1i + p2i + F (i− w1, j − w2, k, -w3)
                profit = dp(w1 - w1_i, w2 - w2_i, w3 - w3_i) + p1_i + p2_i
                #Ambil max dari max_profit atau profit
                #Rumus lain saat barang ke i tidak diambil
                #Bentuk lain F (i − 1, j)
                max_profit = max(max_profit, profit)
        
        #Simpan pada array memo dengan lokasi berdasarkan weight
        memo[(w1, w2, w3)] = max_profit
        return max_profit

    #Profit maksimum saat total weight awal
    max_profit = dp(W1, W2, W3)
    
    # Backtrack to find the items taken
    taken_items = []
    current_w1, current_w2, current_w3 = W1, W2, W3
    #Looping selama weight tidak 0
    while current_w1 > 0 and current_w2 > 0 and current_w3 > 0:
        found = False
        #Looping cek untuk setiap item
        for i in range(n):
            w1_i, w2_i, w3_i = weights[i]
            p1_i, p2_i = profits[i]
            #JIka masik cukup maka
            if current_w1 >= w1_i and current_w2 >= w2_i and current_w3 >= w3_i:
                #Cek apakah barang terambil atau tidak
                #Barang terambil apabila value saat ini adalah jumlah dari value sebelumnya + profit barang
                if dp(current_w1,current_w2,current_w3) == dp(current_w1 - w1_i,current_w2 - w2_i,current_w3 - w3_i) + p1_i + p2_i:
                    #JIka barang diambil maka simpan index
                    taken_items.append(i)
                    #Kurangi weight dengan cost item untuk pengecekan selanjutnya
                    current_w1 -= w1_i
                    current_w2 -= w2_i
                    current_w3 -= w3_i
                    #Jika terambil maka tidak perlu cek barang lain
                    found = True
                    break
                
        #Jika tidak ada lagi item yang dapat dicari maka stop looping
        if not found:
            break

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return max_profit, taken_items, (time.time() - start_time)*10**3, peak
    
    """
    # Initialize the DP table
    dp = [[[0 for _ in range(W3 + 1)] for _ in range(W2 + 1)] for _ in range(W1 + 1)]

    # Fill the DP table
    for w1 in range(W1 + 1):
        for w2 in range(W2 + 1):
            for w3 in range(W3 + 1):
                for i in range(n):
                    w1_i, w2_i, w3_i = weights[i]
                    p1_i, p2_i = profits[i]
                    if w1 >= w1_i and w2 >= w2_i and w3 >= w3_i:
                        dp[w1][w2][w3] = max(dp[w1][w2][w3], dp[w1 - w1_i][w2 - w2_i][w3 - w3_i] + p1_i + p2_i)

    # The maximum profit for the full capacities
    max_profit = dp[W1][W2][W3]
    
    
    # Backtrack to find the items taken
    taken_items = []
    current_w1, current_w2, current_w3 = W1, W2, W3
    while current_w1 > 0 and current_w2 > 0 and current_w3 > 0:
        found = False
        for i in range(n):
            w1_i, w2_i, w3_i = weights[i]
            p1_i, p2_i = profits[i]
            if current_w1 >= w1_i and current_w2 >= w2_i and current_w3 >= w3_i:
                if dp[current_w1][current_w2][current_w3] == dp[current_w1 - w1_i][current_w2 - w2_i][current_w3 - w3_i] + p1_i + p2_i:
                    taken_items.append(i)
                    current_w1 -= w1_i
                    current_w2 -= w2_i
                    current_w3 -= w3_i
                    found = True
                    break
        if not found:
            break
    """
    

def calculateCost(wood, stone, steel):
    rWood = 1
    rStone = 1.5
    rSteel = 2

    return wood*rWood + stone*rStone + steel*rSteel


