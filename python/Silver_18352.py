# bfs 18352
import sys
from collections import deque
input = sys.stdin.readline
# node_num , branch_num , distance , start_point
n , m , k, x = map(int, input().split())

visited = [False] * (n+1)
distance = [0] * (n+1)
adjacent = [ [] for _ in range(n+1) ]
for _ in range(m):
    p,q = map(int, input().split())
    adjacent[p].append(q)

def bfs(start):
    global k
    queue = deque()
    visited[start] = True
    queue.append(start)
    cnt = 0
    while queue:
        node = queue.popleft()
        for n in adjacent[node]:
            if visited[n] == False:
                visited[n] = True
                distance[n] += (distance[node] + 1)
                queue.append(n)

bfs(x)
exists = False
for i in range(1, n+1):
    a = distance[i]
    if a==k:
        exists = True
        print(i)
if not exists:
    print(-1)
