# bfs 1325
import sys
from collections import deque
input = sys.stdin.readline
# node_num , branch_num
n , m = map(int, input().split())
visited = [False] * (n+1)
computers = [0]*(n+1)
adjacent = [ [] for _ in range(n+1) ]
for _ in range(m):
    p,q = map(int, input().split())
    adjacent[q].append(p)

def bfs(start):
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        node = queue.popleft()
        for n in adjacent[node]:
            if visited[n] == False:
                visited[n] = True
                computers[i]+=1
                queue.append(n)

for i in range(1,n+1):
    visited = [False] * (n+1)
    bfs(i)

Max = max(computers)
string = ""
for i in range(1,n+1):
    if computers[i] == Max:
        string += str(i) + ' '
print(string)