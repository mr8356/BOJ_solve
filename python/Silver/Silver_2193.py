#DP
import sys
input = sys.stdin.readline
n = int(input())
D = [[]for _ in range(n+1)]
# [0갯수 , 1갯수]
D[1] = [0,1]
for i in range(2,n+1):
    D[i] = [sum(D[i-1]) , D[i-1][0]]
print(sum(D[n]))