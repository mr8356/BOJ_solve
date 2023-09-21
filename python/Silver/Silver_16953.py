# bfs 16953
import sys
from collections import deque
a, b = map(int,input().split())

def bfs():
  global a,b
  queue = deque()
  queue.append((a,1))
  while queue:
    n, depth = queue.popleft()
    if n==b:
      return depth
    if n*2 <= b:
      queue.append((n*2, depth+1))
    if n*10 + 1 <= b:
      queue.append((n*10+1, depth+1))
  return -1

print(bfs())
