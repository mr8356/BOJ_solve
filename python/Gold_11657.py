#  펠만 - 포드
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
edges = []
dist = [sys.maxsize] * (n+1)
dist[1] = 0
for _ in range(m):
    a,b,w = map(int, input().split())
    edges.append((a,b,w))

isCycle = False
for i in range(n):
    for start,end,w in edges:
        if dist[start] != sys.maxsize:
            distance = dist[start] + w
            if distance < dist[end]:
                if i == n-1:
                    isCycle = True
                dist[end] = distance

if isCycle:
    print(-1)
else:
    for i in dist[2:]:
        # 0과 1번째를 인덱싱으로 제외
        if i == sys.maxsize:
            print(-1)
        else:
            print(i)