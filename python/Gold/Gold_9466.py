import sys
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(node):
  global adjacent, visited, cnt, passedNodes
  if visited[node]:
    return
  visited[node] = True
  passedNodes.append(node)
  wantedTeamate = adjacent[node]
  try:
    idx = passedNodes.index(wantedTeamate)
    cnt += len(passedNodes)-idx
  except:
    dfs(wantedTeamate)

for _ in range(t):
  n = int(input())
  adjacent = list(map((lambda x: int(x) - 1), input().split()))
  visited = [False] * n
  cnt = 0
  for i in range(n):
    passedNodes = []
    dfs(i)
  print(n-cnt)

