#Knapsack
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1-x2)**2 + (y1-y2)**2
    rsum = (r1 + r2)**2
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif d**(1/2) < r1 or d**(1/2) < r2: #inside
        if d**(1/2)+r1 < r2 or d**(1/2)+r2 < r1:
            print(0)
        elif d**(1/2)+r1 == r2 or d**(1/2)+r2 == r1:
            print(1)
        else:
            print(2)
    elif d==rsum:#outside
        print(1)
    elif d>rsum:
        print(0)
    elif d<rsum:
        print(2)