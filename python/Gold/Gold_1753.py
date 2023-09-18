#dijkstra
import sys
from queue import PriorityQueue
input = sys.stdin.readline
V , E = map(int, input().split())
k = int(input())
infinity = 1

adjacent = [[]for _ in range(V+1)]
visited = [False] * (V+1)
for i in range(E):
    n1,n2,w = map(int, input().split())
    adjacent[n1].append((n2,w))
    infinity += w
dist = [infinity] * (V+1)
visited = [False]*(V+1)
dist[k] = 0
queue = PriorityQueue()
queue.put((0,k))
while not queue.empty():
    node = queue.get()[1]
    visited[node] = True
    for i in adjacent[node]:
        distant = dist[node] + i[1]
        if dist[i[0]] > distant:
            dist[i[0]] = distant
            if not visited[i[0]]:
                queue.put((distant , i[0]))
for i in range(1,V+1):
    if dist[i] == infinity:
        print("INF")
    else:
        print(dist[i])