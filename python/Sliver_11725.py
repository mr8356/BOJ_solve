import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
adjacent = [[] for _ in range(n+1)]
parant = [0] * (n+1)
visited = [False] * (n+1)
for i in range(n-1):
  a,b = map(int, input().split())
  adjacent[a].append(b)
  adjacent[b].append(a)

def bfs(start):
  queue = deque()
  visited[start] = True
  queue.append(start)
  while len(queue)!=0:
    node = queue.popleft()
    visited[node] = True
    for i in adjacent[node]:
      if not visited[i]:
        queue.append(i)
        parant[i] = node

bfs(1)
for i in range(2,n+1):
  print(parant[i])