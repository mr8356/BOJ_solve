# 트리의 지름
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
adjacent = [[]for _ in range(n+1)]
for _ in range(n):
    a,b,w = map(int,input().split())
    adjacent[a].append( (b,w) )
    adjacent[b].append( (a,w) )

def bfs(index):
    visited = []