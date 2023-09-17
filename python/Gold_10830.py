import sys
input = sys.stdin.readline
n , b = map(int, input().split())
mat = [list(map(int,input().split())) for _ in range(n)]

# 행렬 대칭시키기
def getVertical(ma):
  matrix = []
  for i in range(n):
    tmp = []
    for j in range(n):
      tmp.append(ma[j][i])
    matrix.append(tmp)
  return matrix

# 벡터의 내적
def innerVector(v1,v2):
  result = 0
  for i in range(n):
    result+=(v1[i]*v2[i])%1000
  return result%1000

# 행렬 내적
def innerMat(m1,m2):
  result = [[0]*n for _ in range(n)]
  m2 = getVertical(m2)
  for i in range(n):
    for j in range(n):
      result[i][j] = innerVector(m1[i],m2[j])
  return result

def squareMat(mat,b):
  if b==1:
    return mat
  if b==2:
    return innerMat(mat,mat)
  elif b%2==0:
    return innerMat(squareMat(mat,b//2),squareMat(mat,b//2))
  else:
    return innerMat(squareMat(mat,b-1),mat)

ans = squareMat(mat,b)

for i in range(n):
  print(*ans[i])
