import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
box = [[0]*(m+1) for _ in range(n+1)]

def insert(x,y):
    if x>0 and x<=n:
        if y>0 and y<=m:
            box[x][y] = -1

def isvalied(x,y):
    if x>0 and x<=n:
        if y>0 and y<=m:
            if box[x][y]!=-1:
                return True
    return False

k = int(input())
for _ in range(k):
    x,y,d = map(int, input().split())
    box[x][y] = -1
    for i in range(d+1):
        j = d-i
        insert(x+i, y+j)
        insert(x+i, y-j)
        insert(x-i, y+j)
        insert(x-i, y-j)

totaltime = sys.maxsize


def dfs(x,y,time):
    global totaltime
    if x == n and y == m:
        totaltime = time
        return
    if isvalied(x+1, y):
        dfs(x+1,y,time+1)
    if isvalied(x, y+1):
        dfs(x,y+1,time+1)

# dfs(1,1,0)
bfs()
if totaltime == sys.maxsize:
    print('NO')
else:
    print('YES')
    print(totaltime)
