# DP
import sys
input = sys.stdin.readline
n = int(input())
A = [[0]for _ in range(n+1)]
for i in range(1,n+1):
    A[i] = list(map(int, input().split()))

for i in range(2,n+1):
    for j in range(i):
        result = A[i][j]
        if j > 0:
            result = A[i-1][j-1] + A[i][j]
        if j < i-1:
            result = max(A[i-1][j]+ A[i][j], result)
        A[i][j] = result
print(max(A[n]))