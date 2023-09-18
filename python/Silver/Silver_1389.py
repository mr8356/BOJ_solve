import sys
input = sys.stdin.readline
n , m = map(int, input().split())
D = [[sys.maxsize]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    D[a][b] = 1
    D[b][a] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
result = sys.maxsize
index = 0
for i in range(1,n+1):
    cnt = 0
    for c in D[i]:
        if c != sys.maxsize:
            cnt += c
    if result > cnt:
        result = cnt
        index = i
print(index)