import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
city = [[0]*(n+1)]
dis = []
for _  in range(n):
    line = [0] + list(map(int, input().split()))
    city.append(line)

for i in range(1,n+1):
    for j in range(1, n+1):
        if city[i][j] == 2:
            temp = []
            for x in range(1,n+1):
                for y in range(1,n+1):
                    if city[x][y] == 1:
                        temp.append(abs(x-i) + abs(y-j))
            dis.append(temp)

comb = list(combinations(dis, m))
mini = sys.maxsize
for c in comb:
    result = [sys.maxsize] * len(c[0])
    for i in range(len(c)):
        for j in range(len(c[0])):
            result[j] = min(c[i][j] , result[j])
    mini = min(mini, sum(result))
print(mini)
