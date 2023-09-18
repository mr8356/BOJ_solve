# DP[i] ==> i까지 최대길이
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
DP = [0] * n
result = 1
for i in range(1,n):
    if num[i] <= num[i-1]:
        DEC[i] = DEC[i-1] + 1
    else:
        DEC[i] = 1
    if num[i] >= num[i-1]:
        INC[i] = INC[i-1] + 1
    else:
        INC[i] = 1
    result = max(result , DEC[i] , INC[i])
print(result)