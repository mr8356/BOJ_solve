#플로이드-워셜
import sys
input = sys.stdin.readline
n = int(input())
D = [[]]

for _ in range(n):
    D.append([0] + list(map(int, input().split())))
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            if D[i][j] ==1:
                continue
            if D[i][k] ==1 and D[k][j]==1:
                D[i][j] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(D[i][j],end=' ')
    print()

