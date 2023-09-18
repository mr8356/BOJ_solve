#Knapsack
import sys
input = sys.stdin.readline
t = int(input())

def knapsack(n, coins, cost):
    DP = [[0] * (cost + 1) for _ in range(n+1)]
    DP[0][0] = 1
    for i in range(1, n+1):
        coin = coins[i]
        for j in range(0, cost+1):
            # cnt = DP[i-1][j]
            # if j%coin == 0:
            #     cnt+=1
            cnt = j//coin
            for k in range(0,coin*cnt +1,coin):
                DP[i][j] += DP[i-1][j-k]
    print(DP[n][cost])

for _ in range(t):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    cost = int(input())
    knapsack(n, coins, cost)
