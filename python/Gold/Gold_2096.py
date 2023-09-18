#DP - 슬라이드 윈도우
import sys
input = sys.stdin.readline
n = int(input())
DP = [0]*3
RD = [0]*3
for i in range(n):
    li = list(map(int, input().split()))
    max_result = []
    min_result = []
    max_result.append(max(DP[0], DP[1]) + li[0])
    max_result.append(max(DP[0], DP[1], DP[2]) + li[1])
    max_result.append(max(DP[2], DP[1]) + li[2])
    min_result.append(min(RD[0], RD[1]) + li[0])
    min_result.append(min(RD[0], RD[1], RD[2]) + li[1])
    min_result.append(min(RD[2], RD[1]) + li[2])
    DP = max_result
    RD = min_result

print(max(DP),end=' ')
print(min(RD))