# dijkstra
import sys
from queue import PriorityQueue
input = sys.stdin.readline

n,m,x = map(int,input().split())
adjacent = [[]for _ in range(n+1)]
for i in range(m):
    a,b,w = map(int,input().split())
    adjacent[a].append((b,w))

def dijkstra(index , goal):
    dist = [sys.maxsize] * (n+1)
    visited =[False] *(n+1)
    dist[index] = 0
    queue = PriorityQueue()
    queue.put((0,index))
    while queue.qsize()!=0:
        node = queue.get()
        if visited[node[1]]:
            continue
        if node[1] == goal:
            return dist[goal]
        visited[node[1]] = True
        for i in adjacent[node[1]]:
            distance = node[0] + i[1]
            if distance < dist[i[0]]:
                dist[i[0]] = distance
                queue.put((distance , i[0]))

Max = 0
for i in range(1,n+1):
    if i == x:
        continue
    time = dijkstra(i,x) + dijkstra(x, i)
    if time>Max:
        Max = time
    
print(Max)