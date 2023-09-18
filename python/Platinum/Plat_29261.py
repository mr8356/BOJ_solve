import math
p = int(input())

A = [0]*(p+1)
# w = [p]
cnt = 1
# initialize
for i in range(2,p+1):
    A[i] = i

for i in range(2,int(math.sqrt(p))+1):
    if A[i] == 0:
        continue
    for j in range(i+i , p+1, i):
        A[j] = 0

def find(n):
  global cnt
  sum = n-1
  li = []
  for i in range(2 ,sum//2+1):
    if A[i]!=0:
        if A[sum-i]!=0:
          li = (i,sum-i)
  if len(li) != 0:
    find(li[0])
    find(li[1])
    cnt+=2

find(p)
print(cnt)
