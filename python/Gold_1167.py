# BFS GOLD2
# 그래프에서 서로 가장 멀리 떨어져있는 두 노드는
# 임의의 한 노드에서 가장 떨어진 노드 중 하나이다
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
visited = [False]*(n+1)
adjacent = [ [] for _ in range(n+1) ]

for i in range(1,n+1):
    req = list(map(int , input().split()))[1:-1]
    for j in range(0,int(len(req)/2)):
        distance = req[j+1]
        adjacent[i].append( (req[j] , distance) )
        adjacent[req[j]].append( (i , distance) )
        j+=2

distance = [0] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        node = queue.popleft()
        for i in adjacent[node]:
            if visited[i[0]] == False:
                queue.append(i[0])
                visited[i[0]]=True
                distance[i[0]]= distance[node]+i[1]

bfs(1)
result_index = distance.index( max(distance) )
visited = [False]*(n+1)
distance = [0] * (n+1)
bfs(result_index)
print(max(distance))