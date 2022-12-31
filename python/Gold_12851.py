# 13549
# BFS 찾기
import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n , k  = map(int , input().split())
dist =[sys.maxsize] *(10**6+1) #+ [0] *(10**6+1)
dist[n] = 0
cnt = 0
def dijkstra():
    global cnt
    queue = PriorityQueue()
    queue.put((0,n))
    while queue.qsize() != 0:
        d,p = queue.get()
        if 0<=p*2<=10**6:
            if p == k:
                cnt += 1
                continue
            if p > k:
                if dist[p] + 1 <= dist[p-1]:
                    dist[p-1] = dist[p] + 1
                    queue.put((dist[p-1],p-1))
            else:
                for i in [p-1 , p+1 , p*2]:
                    if dist[p]+1 <= dist[i]:
                        dist[i] = dist[p] + 1
                        queue.put((dist[i],i))
dijkstra()
print(dist[k])
print(cnt)
