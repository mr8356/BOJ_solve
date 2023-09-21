# 소수 구하기
# 에라토스테네스의 체
import math
m, n = map(int,input().split())
A = [0]*(n+1)
# initialize
for i in range(2,n+1):
    A[i] = i

for i in range(2,int(math.sqrt(n))+1):
    if A[i] == 0:
        continue
    for j in range(i+i , n+1, i):
        A[j] = 0

for i in range(m , n+1):
    if A[i]!=0:
        print(i)