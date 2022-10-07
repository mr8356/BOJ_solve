import sys
from collections import deque
input = sys.stdin.readline
n= int(input())
adjacent = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)
time = [0]*(n+1)
# result = [0]*(n+1)
for i in range(1,n+1):
    inline = list(map(int , input().split()))[:-1]
    time[i] = inline[0]
    for j in range(1,len(inline)):
        adjacent[inline[j]].append(i)
        in_degree[i] +=1

queue = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        # result = time[i]
        queue.append(i)

while queue:
    node = queue.popleft()
    for i in adjacent[node]:
        if in_degree[i] == 1:
            time[i] += time[node]
            queue.append(i)
        in_degree[i] -= 1

for i in range(1, n+1):
    print(time[i])