# 위상 정렬
import sys
from collections import deque

input = sys.stdin.readline
n= int(input())
adjacent = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)
time = [0]*(n+1)
result = [0]*(n+1)
for i in range(1,n+1):
    inline = list(map(int , input().split()))[:-1]
    time[i] = inline[0]
    for j in range(1,len(inline)):
        adjacent[inline[j]].append(i)
        in_degree[i] +=1

queue = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        result[i] = time[i]
        queue.append(i)

while queue:
    node = queue.popleft()
    for i in adjacent[node]:
        # 두개의 건물이 지어져야 할때, 최대 시간이 체택
        result[i] = max( result[node]+time[i] , result[i])
        if in_degree[i] == 1:
            queue.append(i)
        in_degree[i] -= 1

for i in range(1, n+1):
    print(result[i])