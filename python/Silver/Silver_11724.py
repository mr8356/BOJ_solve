#DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n , m = map(int , input().split())
adjacent = [[] for _ in range(n)]
visited = [False]*n
cnt = 0

def DFS(start):
    visited[start] = True
    for node in adjacent[start]:
        if visited[node] == False :
            DFS(node)

for i in range(m):
    u , v = map(int , input().split())
    adjacent[u-1].append(v-1)
    adjacent[v-1].append(u-1)
for node in range(n):
    if visited[node] == False:
        DFS(node)
        cnt+=1
print(cnt)