# DP
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
DP = [0] * (n) # n(번째)를 포함하는 n까지의 부분수열의 (가장 큰 값, 길이)
length = 0
DP[0] = (A[0], 1)
for i in range(1,n):
  tmp = list(filter(lambda x: x[0] < A[i], DP[:i]))
  if len(tmp) == 0:
    DP[i] = (A[i], 1)
  else:
    mx=0
    for j in range(len(tmp)):
      mx = max(tmp[j][1], mx)
    DP[i] = (A[i], mx + 1)

mx = 0
for i in range(n):
  mx = max(mx, DP[i][1])
print(mx)