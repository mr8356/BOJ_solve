#DP
import sys
input = sys.stdin.readline
n = int(input())
D = [[0]*(10) for _ in range(n+1)]
D[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    D[i][0] = D[i-1][1]
    D[i][9] = D[i-1][8]
    for j in range(1,9):
        D[i][j] = D[i-1][j-1] + D[i-1][j+1]
print(sum(D[n])%(10**9))