# dfs & bfs
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)

n, m, v = map(int , input().split())
visited = [False]*(n+1)
adjacent = [ [] for _ in range(n+1) ]

def dfs(start):
    visited[start]=True
    print(str(start)+' ')
    adjacent[start].sort()
    for i in adjacent[start]:
        if visited[i] == False:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while len(q)!=0:
        node = q.popleft()
        print(str(node)+' ')
        adjacent[node].sort()
        for i in adjacent[node]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True


for _ in range(m):
    a,b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)
dfs(v)
visited = [False]*(n+1)
print('\n')
bfs(v)
