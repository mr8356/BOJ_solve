import sys
input = sys.stdin.readline
n, m, goal, init = map(int, input().split())
A = list(map(int, input().split()))
D = [0] * (n+1)
A[0] += init
if A[0] < goal:
    D[1] = 1
for i in range(1,n):
    A[i]+=A[i-1]
    if A[i] < goal:
        D[i+1] = 1
for i in range(2,n+1):
    D[i] += D[i-1]
for _ in range(m):
    s,e = map(int, input().split())
    print(D[e-1] - D[s-1])