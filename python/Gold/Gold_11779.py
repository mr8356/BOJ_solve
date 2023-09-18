import sys
from heapq import heappush, heappop
queue = []
input = sys.stdin.readline
n = int(input())
m = int(input())
adjacent = [[]for _ in range(n+1)]
route = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int, input().split())
    adjacent[a].append((b,w))
dist = [sys.maxsize] * (n+1)
A, B = map(int, input().split())
dist[A] = 0
visited = [False] * (n+1)
heappush(queue,(0,A))
while visited[B] == False:
    d, node = heappop(queue)
    visited[node] = True
    route[node].append(node)
    for i in adjacent[node]:
        distance = d + i[1]
        if not visited[i[0]] and distance < dist[i[0]]:
            dist[i[0]] = distance
            route[ i[0] ] = route[node].copy()
            heappush(queue,(distance, i[0]))
print(dist[B])
print(len(route[B]))
for i in route[B]:
    print(i,end=' ')