import sys
input = sys.stdin.readline
n, b = map(int, input().split())
mat = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(n)]


# 행렬 내적
def innerMat(m1, m2):
    result = [[0]*n for _ in range(n)]
    # m2 = getVertical(m2)
    for i in range(n):
        for j in range(n):
            add = 0
            for k in range(n):
                add += (m1[i][k]*m2[k][j]) % 1000
            result[i][j] = add % 1000
    return result


def squareMat(mat, b):
    if b == 1:
        return mat
    if b % 2 == 0:
        mat = squareMat(mat, b//2)
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                add = 0
                for k in range(n):
                    add += (mat[i][k]*mat[k][j]) % 1000
                result[i][j] = add % 1000
        return result
    else:
        return innerMat(squareMat(mat, b-1), mat)


ans = squareMat(mat, b)

for i in range(n):
    print(*ans[i])
