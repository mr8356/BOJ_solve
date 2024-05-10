# 비트필드를 이용한 다이나믹 프로그래밍 -> dp 테이블 말고 딕셔너리 사용
import sys
input = sys.stdin.readline
n = int(input())
INF = sys.maxsize
adjacent = [] # 인접행렬
for _ in range(n):
    adjacent.append(list(map(int, input().split())))
bit_range = 1 << n
dp = {}

# 앞으로의 거리
def dfs(now, visited):
    # 전부 다 탐색을 끝났다면?
    if visited == bit_range - 1:
        if adjacent[now][0] != 0:
            return adjacent[now][0] # 어차피 출발점은 0임, 앞으로의 거리므로 마지막 거리
        else:
            return INF
    # 이미 구한 구간이면 메모리제이션
    if (now, visited) in dp:
        return dp[(now, visited)]
    # 탐색 시작 & 최소 시간 구하기
    min_cost = INF
    for i in range(n):
        if adjacent[now][i] == 0:
            continue
        if (1<<i) & visited == 0:
            min_cost = min(dfs(i, (visited | 1<<i)) + adjacent[now][i], min_cost)
    dp[(now, visited)] = min_cost
    return min_cost
print(dfs(0, 1<<0))