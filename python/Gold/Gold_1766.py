import heapq
hq = []
n,m  = map(int, input().split())
adjacent = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
visited = [False] * (n+1)
result = []
for _ in range(m):
  a, b = map(int, input().split())
  in_degree[b] += 1
  adjacent[a].append(b)

for i in range(1,n+1):
  heapq.heappush(hq, (in_degree[i],i))

try:
  while True:
    degree,node = heapq.heappop(hq)
    if visited[node]:
      continue
    visited[node] = True
    for child in adjacent[node]:
        in_degree[child] -= 1
        heapq.heappush(hq, (in_degree[child],child))
    result.append(node)
except:
  print(*result)