import time
import tracemalloc


def unbounded_knapsack(n, W1, W2, W3, weights, profits):
    start_time = time.time()
    tracemalloc.start()
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
    
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return max_profit, taken_items, (time.time() - start_time)*10**3, peak

def calculateCost(wood, stone, steel):
    rWood = 1
    rStone = 1.5
    rSteel = 2

    return wood*rWood + stone*rStone + steel*rSteel


