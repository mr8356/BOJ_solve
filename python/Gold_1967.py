# 트리의 지름
# BFS
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
adjacent = [[]for _ in range(n+1)]
for _ in range(1,n):
    a,b,w = map(int,input().split())
    adjacent[a].append( (b,w) )
    adjacent[b].append( (a,w) )
dist = [0]*(n+1)
def bfs(index):
    visited = [False] * (n+1)
    queue = deque()
    queue.append(index)
    while queue:
        node = queue.popleft()
        visited[node] = True
        for i in adjacent[node]:
            if not visited[i[0]]:
                queue.append(i[0])
                dist[i[0]] = dist[node] + i[1]
    return max(dist)

bfs(1)
node = dist.index(bfs(1))
dist = [0]*(n+1)
print(bfs(node))