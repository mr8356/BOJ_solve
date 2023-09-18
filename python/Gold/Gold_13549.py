# 13549
# BFS 찾기
import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n , k  = map(int , input().split())
dist =[sys.maxsize] *(10**6+1)
dist[n] = 0

def dijkstra():
    queue = PriorityQueue()
    queue.put((0,n))
    while queue.qsize() != 0:
        d,p = queue.get()
        if 0<=p*2<=10**6:
            if p == k:
                return d
            if p > k:
                if dist[p] + 1 < dist[p-1]:
                    dist[p-1] = dist[p] + 1
                    queue.put((dist[p-1],p-1))
            else:
                if dist[p] < dist[p*2]:
                    dist[p*2] = dist[p]
                    queue.put((dist[p*2] ,p*2))
                for i in [p-1 , p+1]:
                    if dist[p]+1 < dist[i]:
                        dist[i] = dist[p] + 1
                        queue.put((dist[i],i))
            
print(dijkstra())


# def bfs():
#     queue = deque()
#     queue.append(n)
#     while queue:
#         p = queue.popleft()
#         if p==k:
#             return dist[p]
#         node = [p-1 , p+1]
#         if p > k:
#             node = [p-1]
#         else:
#             if 0<=p*2<=10**6 and dist[p] < dist[p*2]:
#                 queue.append(p*2)
#                 dist[p*2] = dist[p]
#         for i in node:
#             if 0<=i<=10**6 and dist[p]+1 < dist[i]:
#                 queue.append(i)
#                 dist[i] = dist[p] +1
# print(bfs())