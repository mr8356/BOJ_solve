import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


sa = [0]*(n+1)
sb = [0]*(m+1)
for i in range(n):
    sa[i+1] = sa[i] + a[i]
for i in range(m):
    sb[i+1] = sb[i] + b[i]

a_list = []
b_list = []
cnt = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        a_list.append(sa[j] - sa[i-1])

for i in range(1, m+1):
    for j in range(i, m+1):
        b_list.append(sb[j] - sb[i-1])

a_list.sort()
b_list.sort()

for aget in a_list:
    num = bisect_right(b_list, t-aget) - bisect_left(b_list, t-aget)
    cnt += num
cnt += bisect_right(a_list, t) - bisect_left(a_list, t)
cnt += bisect_right(b_list, t) - bisect_left(b_list, t)

if t == 0:
  print(cnt+1)
else:
  print(cnt)
