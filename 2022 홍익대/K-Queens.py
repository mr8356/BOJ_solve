import sys
input = sys.stdin.readline
n, k = map(int, input().split())
r,c = map(int, input().split())
king = (r,c)
queens = []
def isInside(x,y):
    if x>=1 and x <= n:
        if y>=1 and y<=n:
            return True
    return False

def isBlock(x,y):
    if isInside(x, y):
        if box[x][y] == 1:
            return True
        else: 
            return False
    else:
        return True

for _ in range(k):
    x, y = map(int, input().split())
    queens.append((x,y))
box = [[0]*(n+1) for _ in range(n+1)]
for x,y in queens:
    box[x] = [1]*(n+1)
    for i in range(n+1):
        if box[i][y] == 0:
            box[i][y] = 1
    for i in range(1,n):
        if isInside(x+i, y+i):
            box[x+i][y+i] = 1
        else:
            break
    for i in range(1,n):
        if isInside(x-i, y-i):
            box[x-i][y-i] = 1
        else:
            break


if isBlock(r,c+1)and isBlock(r,c-1) and isBlock(r+1,c+1) and isBlock(r+1,c-1) and isBlock(r-1,c+1) and isBlock(r-1,c-1) and isBlock(r+1,c) and isBlock(r-1,c):
    if box[r][c] == 1:
        print("CHECKMATE")
    else:
        print("STALEMATE")
elif box[r][c] == 1:
    print("CHECK")
else:
    print("NONE")

