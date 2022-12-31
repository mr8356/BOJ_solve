n,m = map(int, input().split())
DP = [[0] * (m+1) for _ in range(n+1)]

#initialize
for i in range(1,n+1):
    for j in range(0,m+1):
        if i==j:
            DP[i][j] = 1
        elif j==1:
            DP[i][j] = i
        elif j==0:
            DP[i][j] = 1

for i in range(2,n+1):
    for j in range(2,m+1):
        if DP[i][j] == 0:
            DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

print(DP[n][m])