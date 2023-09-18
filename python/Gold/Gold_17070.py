import sys
input = sys.stdin.readline
n = int(input())
tile = [list(map(int, input().split())) for _ in range(n)]

DP = [[[0]*(n) for _ in range(n)]
      for _ in range(3)]  # 파이프 끝점이 x,y 좌표로 도달할수 있는 방법들
# 0 : 오른쪽 방향, 1 : 아래 방향, 2 : 대각선 방향

# 문제에서 가장 처음 파이프는 (1, 1)와 (1, 2)차지하는 오른쪽 파이프하고 명시돼있음
# 0(오른쪽 방향), (1,2) -> (0,1)
DP[0][0][1] = 1
for i in range(n):
    for j in range(1, n):
        if DP[0][i][j] > 0 and j+1 < n and tile[i][j+1] == 0:
            DP[0][i][j+1] += DP[0][i][j]
        if DP[1][i][j] > 0 and i+1 < n and tile[i+1][j] == 0:
            DP[1][i+1][j] += DP[1][i][j]
        if DP[2][i][j] > 0:  # 대각선 방향
            if j+1 < n and tile[i][j+1] == 0:  # 옆으로 갈때
                DP[0][i][j+1] += DP[2][i][j]
            if i+1 < n and tile[i+1][j] == 0:  # 밑으로 갈때
                DP[1][i+1][j] += DP[2][i][j]
        if i+1 < n and j+1 < n and tile[i][j+1]+tile[i+1][j]+tile[i+1][j+1] == 0:
            DP[2][i+1][j+1] += (DP[0][i][j]+DP[1][i][j]+DP[2][i][j])
        # print(i,j,(DP[0][i][j],DP[1][i][j],DP[2][i][j]))

print(DP[0][n-1][n-1]+DP[1][n-1][n-1]+DP[2][n-1][n-1])
