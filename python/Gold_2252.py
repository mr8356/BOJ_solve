# 위상 정렬 UNDO!!
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
adjacent = [[]for _ in range(n+1)]
in_degree = [0]*(n+1) # 진입 차수 리스트
for i in range(m):
    a,b = map(int, input().split()) # a -> b
    adjacent[a].append(b)
    in_degree[b] += 1
while True:
    # 0인것 탐색
    for i in range(1,n+1):
        if in_degree[i] == 0:
            print(i,end=' ')
            for j in adjacent[i]:
                in_degree[j] -= 1
            # indegree[i] 를 삭제 해야 한다
            break