import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
n,m,s,e = map(int,input().split())
inp = []
degree = [0]*(n+1)
for i in range(m):
  u,v = map(int,input().split())
  inp.append((u,v))
  # adjacent[v].append(u)

def bfs(start, adjacent):
    visited = [False] * (n+1)
    queue = deque()
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        node = queue.popleft()
        if node==e:
          if len(queue) == 0:
            return True
          else:
            return False
        for i in adjacent[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i]=True
    return False

def tempt(idx,adjacent,ans):
  global m
  if idx == m:
    if bfs(s,adjacent):
      print(*ans)
      exit(0)
    else:
      return
  u,v = inp[idx]
  li1 = adjacent.copy()
  li1[v].append(u)
  ans.append(0)
  tempt(idx+1,li1,ans[::])
  li2 = adjacent.copy()
  li2[u].append(v)
  ans[idx] = 1
  tempt(idx+1,li2,ans[::])

a = [[]for _ in range(n+1)]
tempt(0,a,[])
print(-1)
