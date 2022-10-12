#dijkstra
import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
m = int(input())
infinity = 1
adjacent = [[]for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    n1,n2,w = map(int, input().split())
    adjacent[n1].append((n2,w))
    infinity+=w
start , end = map(int,input().split())
dist = [infinity] * (n+1)
visited = [False]*(n+1)
queue = PriorityQueue()
queue.put((0,start))
dist[start] = 0
while not queue.empty():
    node = queue.get()[1]
    if visited[node]:
        continue
    visited[node] = True
    for i in adjacent[node]:
        distance = dist[node] + i[1]
        if dist[i[0]] > distance:
            dist[i[0]] = distance
            queue.put((distance , i[0]))
print(dist[end])