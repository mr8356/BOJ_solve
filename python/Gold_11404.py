import sys
input =  sys.stdin.readline
n = int(input())
m = int(input())
D = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    D[i][i] = 0

for _ in range(m):
    a,b,w = map(int, input().split())
    D[a][b] = min(D[a][b] , w)
for k in range(1,n+1):#경유지
    for i in range(1,n+1):
        for j in range(1,n+1):
            D[i][j] = min(D[i][k] + D[k][j], D[i][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if D[i][j] == sys.maxsize:
            print(0,end=' ')
        else:
            print(D[i][j],  end=' ')
    print()
