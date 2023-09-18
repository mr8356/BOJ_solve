import sys
input = sys.stdin.readline
n = int(input())
T = [0] * (n+1)
P = [0] * (n+1)
D = [0] * (n+1)
for i in range(n,0,-1):
    T[i] , P[i] = map(int, input().split())
for i in range(1,n+1):
    if T[i] <= i:
        D[i] = max(D[i-T[i]] + P[i] , D[i-1])
    else:
        D[i] = max(D[i] , D[i-1])
print(D[n])