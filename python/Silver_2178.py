# BFS
# 미로 찾기

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
map = [ [] for _ in range(n) ]

for i in range(n):
    numbers = list(input())
    for j in range(m):
        map[i].append(int(numbers[j]))

def isInside(x , y):
    if 0<= x <n:
        if 0<= y < m:
            return True
    return False

def bfs():
    queue = deque()
    queue.append((0,0,1))
    while queue:
        node = queue.popleft()
        if isInside(node[0]+1, node[1])  and map[node[0]+1][node[1]]==1:
            if node[0]+1 == n-1 and node[1] == m-1:
                print(node[2]+1)
                break
            queue.append((node[0]+1, node[1], node[2]+1))
            map[node[0]+1][node[1]] = 0

        if isInside(node[0]-1, node[1])  and map[node[0]-1][node[1]]==1:
            if node[0]-1 == n-1 and node[1] == m-1:
                print(node[2]+1)
                break
            queue.append((node[0]-1, node[1], node[2]+1))
            map[node[0]-1][node[1]] = 0

        if isInside(node[0], node[1]+1)  and map[node[0]][node[1]+1]==1:
            if node[0] == n-1 and node[1]+1 == m-1:
                print(node[2]+1)
                break
            queue.append((node[0], node[1]+1, node[2]+1))
            map[node[0]][node[1]+1] = 0

        if isInside(node[0], node[1]-1)  and map[node[0]][node[1]-1]==1:
            if node[0] == n-1 and node[1]-1 == m-1:
                print(node[2]+1)
                break
            queue.append((node[0], node[1]-1, node[2]+1))
            map[node[0]][node[1]-1] = 0

bfs()
