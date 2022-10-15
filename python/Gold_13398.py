#DP
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
# D[n] ==> n을 포함한 수열의 최댓값 (삭제 X)
L = [0] * (n) # 왼쪽에서 부터 탐색한 D
R = [0] * (n) # 오른쪽 부터 탐색한 D

# 수를 제거 : L[i-1] + R[i+1] ==> i를 제외한 최대합
# 수를 제거X : result
L[0] = A[0]
result = L[0]
for i in range(1,n):
    L[i] = max(L[i-1] + A[i] , A[i])
    result = max(result , L[i])

R[n-1] = A[n-1]
for i in range(n-2,-1,-1):
    R[i] = max(R[i+1] + A[i] , A[i])

for i in range(1,n-1):
    result = max(L[i-1] + R[i+1], result)

print(result)