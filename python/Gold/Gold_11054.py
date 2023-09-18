# DP
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
L = [0] * (n) # 왼쪽(0)부터 시작해서 n(번째)를 축으로 하는 n-1까지의 부분증가수열의 길이
R = [0] * (n) # 오른쪽(length-1)부터 시작해서 n(번째)를 축으로 하는 n+1까지의 부분 감소 수열의 길이
# L[n]+R[n]+1 : n번째 수를 포함하는 바이토닉수열의 길이

if n==1:
  print(1)
  exit()

L[0] = (A[0], 0) # n번째수의 크기, 수열길이
for i in range(1,n):
  tmp = list(filter(lambda x: x[0] < A[i], L[:i]))
  if len(tmp) == 0:
    L[i] = (A[i], 0)
  else:
    mx=0
    for j in range(len(tmp)):
      mx = max(tmp[j][1], mx)
    L[i] = (A[i], mx + 1)

R[n-1] = (A[n-1], 0)
for i in range(n-2,-1,-1):#n-2~0
  tmp = list(filter(lambda x: x[0] < A[i], R[i+1::]))
  if len(tmp) == 0:
    R[i] = (A[i], 0)
  else:
    mx=0
    for j in range(len(tmp)):
      mx = max(tmp[j][1], mx)
    R[i] = (A[i], mx + 1)

length = 0
for i in range(n):
  length = max(L[i][1]+R[i][1]+1, length)
print(length)