#DP
# 아주 중요... 풀이 봄..
import sys
sys.setrecursionlimit(10**4)
A = input().strip()
B = input().strip()
DP = [[0]*(len(B)+1) for _ in range(len(A) + 1)]
for i in range(1,len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i][j-1] ,DP[i-1][j])
ans = []
def getText(x , y):
    if x == 0 or y == 0:
        return
    if A[x-1] == B[y-1]:
        ans.append(A[x-1])
        getText(x-1, y-1)
    else:
        if DP[x-1][y] > DP[x][y-1]:
            getText(x-1, y)
        else:
            getText(x, y-1)
getText(len(A), len(B))
print(DP[len(A)][len(B)])
for _ in range(len(ans)):
    print(ans.pop(),end='')
    
