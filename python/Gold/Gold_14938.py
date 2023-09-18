import sys
from queue import PriorityQueue
input = sys.stdin.readline
n, k, m = map(int, input().split())
items = [0] + list(map(int, input().split()))
adjacent = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int, input().split())
    adjacent[a].append((b,w))
    adjacent[b].append((a,w))

def dijkstra(index):
    visited = [False] * (n+1)
    dist = [sys.maxsize] * (n+1)
    dist[index] = 0
    queue = PriorityQueue()
    queue.put((0, index))
    while queue.qsize() != 0:
        node = queue.get()[1]
        visited[node] = True
        for i in adjacent[node]:
            # i[0] node number , i[1] weight
            distance = dist[node] + i[1]
            if distance < dist[i[0]] and not visited[i[0]]:
                dist[i[0]] = distance
                queue.put((distance , i[0]))
    num_item = 0
    for i in range(1,n+1):
        d = dist[i]
        if d > k:
            continue
        num_item += items[i]
    return num_item

Max = 0
for index in range(1,n+1):
    result = dijkstra(index)
    if result>Max:
        Max = result
print(Max)