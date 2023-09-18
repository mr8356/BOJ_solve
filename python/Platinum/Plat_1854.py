import sys
from queue import PriorityQueue
input = sys.stdin.readline
n, m, k = map(int, input().split())
adjacent = [[] for _ in range(n+1)]
dist = [[sys.maxsize] * k for _  in range(n+1)]
for i in range(m):
    a, b, w = map(int,input().split())
    adjacent[a].append((b,w))
def dijkstra(start):
    queue = PriorityQueue()
    queue.put((0,start)) #dis / node
    dist[start][0] = 0
    while not queue.empty():
        pop = queue.get()
        d = pop[0]
        node = pop[1]
        for i in adjacent[node]:
            distance = d + i[1]
            if dist[i[0]][-1] > distance:
                dist[i[0]][-1] = distance
                dist[i[0]].sort()
                queue.put((distance, i[0]))
dijkstra(1)
for i in range(1,n+1):
    d = dist[i][k-1]
    if d == sys.maxsize:
        print(-1)
    else:
        print(d)

