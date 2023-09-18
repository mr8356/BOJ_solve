import sys
input = sys.stdin.readline
n, m = map(int, input().split())
bite = []
cost = []
bite = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
size = sum(cost)
DP = [[0] * (size+1) for _ in range(n+1)]
for i in range(1,n):
    for j in range(0,size+1):
        if j>=cost[i]:
            # 이용할때 vs 이용안하고 그대로 일때
            DP[i][j] = max(bite[i] + DP[i-1][j-cost[i]] , DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j];

for j in range(0,size+1):
    if j>=cost[n]:
        # 이용할때 vs 이용안하고 그대로 일때
        DP[n][j] = max(bite[n] + DP[n-1][j-cost[n]] , DP[n-1][j])
    else:
        DP[n][j] = DP[n-1][j];
    if DP[n][j] >= m:
        print(j)
        break
