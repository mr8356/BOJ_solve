#Knapsack
import sys
input = sys.stdin.readline
n,t = map(int, input().split())
times = [0]
points = [0]
for _ in range(n):
    time, score = map(int, input().split())
    times.append(time)
    points.append(score)
DP = [[0]*(t+1) for _ in range(n+1)]
for i in range(1,n+1):
    time = times[i]
    p = points[i]
    for j in range(1,t+1):
        if j >= time:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-time] + p)
        else:
            DP[i][j] = DP[i-1][j]
print(max(DP[n]))