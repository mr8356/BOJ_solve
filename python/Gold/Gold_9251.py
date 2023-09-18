import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
A = input().strip()
B = input().strip()
D = [[0]*(len(B)+1) for _ in range(len(A)+1)]

# iteration
# for i in range(1,len(A)+1):
#     for j in range(1, len(B)+1):
#         if A[i-1] == B[j-1]:
#             D[i][j] = D[i-1][j-1] + 1
#         else:
#             D[i][j] = max(D[i-1][j], D[i][j-1])

# recursion
def getD(i , j):
    if i==0 or j==0:
        return 0
    if D[i][j] == 0:
        if A[i-1] == B[j-1]:
            D[i][j] = getD(i-1, j-1) + 1
        else:
            D[i][j] = max(getD(i-1,j), getD(i, j-1))
    return D[i][j]

print(getD(len(A), len(B)))

