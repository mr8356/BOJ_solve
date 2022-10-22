# 위상 정렬
import sys
from collections import deque
input = sys.stdin.readline
test = int(input())
i
time = []
ans = [0]*(test)
for t in range(test):
    n,k = map(int,input().split())
    time = [0] + list(map(int, input().split()))
    result = [0] * (n+1)
    adjacent = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(k):
        a,b = map(int,input().split())
        adjacent[a].append(b)
        indegree[b] += 1
    x = int(input())

    #위상정렬 start
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]
    while queue:
        node = queue.popleft()
        if node == x:
            break
        for c in adjacent[node]:
            result[c] = max(result[c],result[node] + time[c])
            if indegree[c] == 1:
                queue.append(c)
            indegree[c] -= 1
    ans[t] = result[x]
    #위상정렬 end

for t in range(test):
    print(ans[t])
    
