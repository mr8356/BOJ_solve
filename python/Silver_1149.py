# DP ITERATION
import sys
input = sys.stdin.readline

n = int(input())
costs = [[]]
D = [[-1]*(3) for _ in range(n+1)]

for i in range(n):
    # R 0, G 1, B 2
    costs.append(list(map(int, input().split())))
D[1] = costs[1]
for i in range(2,n+1):
    for c in range(3):
        D[i][c] = min(D[i-1][(c+1)%3], D[i-1][(c+2)%3]) + costs[i][c]

print( min( D[n][0], D[n][1], D[n][2] ) )


############################################

# DP RECURSION
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
costs = [[]]
D = [[-1]*(3) for _ in range(n+1)]

for i in range(n):
    # R 0, G 1, B 2
    costs.append(list(map(int, input().split())))
D[1] = costs[1]

def getD(i,c):
    if D[i][c] == -1:
        D[i][c] = min(getD(i-1,(c+1)%3), getD(i-1,(c+2)%3)) + costs[i][c]
    return D[i][c]

print( min( getD(n,0), getD(n,1), getD(n,2) ) )