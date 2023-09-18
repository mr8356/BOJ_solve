# 1697
# BFS 찾기
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n , k  = map(int , input().split())
dist =[0] *(10**6+1)
def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        p = queue.popleft()
        if p==k:
            return dist[p]
        node = [p-1 , p+1 , p*2]
        if p > k:
            node = [p-1]
        for i in node:
            if 0<=i<=10**6 and not dist[i]:
                queue.append(i)
                dist[i] = dist[p] +1
print(bfs())