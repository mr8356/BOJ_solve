import sys
input = sys.stdin.readline
k = int(input())
for _ in range(k):
  n = int(input())
  A = []
  A.append(list(map(int, input().split())))
  A.append(list(map(int, input().split())))
  DP = [[0] * (n) for _ in range(2)]
  DP[0][0] = A[0][0]
  DP[1][0] = A[1][0]
  for i in range(1,n):
    for j in range(2):
      DP[j][i] = DP[(j+1)%2][i-1] + A[j][i]
      if i>=2:
        DP[j][i] = max(DP[j][i-2]+A[j][i], DP[(j+1)%2][i-2]+A[j][i], DP[j][i])
  print(max(DP[0][n-1], DP[1][n-1]))
  