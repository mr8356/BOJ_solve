#BFS
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
box = []
visited = [[False] * m for i in range(n)]
brvisited = [[False] * m for i in range(n)]
ans = sys.maxsize
for _ in range(n):
    li = list(input().strip())
    box.append(li)

def isInside(x,y):
    if 0<=x<n:
        if 0<=y<m:
            return True
    return False

def bfs():
    global ans
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append((0,0,1,0)) # x,y,time, break = yes :1 no : 0
    while len(queue) != 0:
        x,y,time,isBreak = queue.popleft()
        if x == n-1 and y == m-1:
            ans = min(ans, time)
        if isBreak == 0:
            for i in range(4):
                if isInside(x+dx[i], y+dy[i]) and not visited[x+dx[i]][y+dy[i]]:
                    if box[x+dx[i]][y+dy[i]] == '0':
                        queue.append((x+dx[i],y+dy[i],time+1,0))
                        visited[x+dx[i]][y+dy[i]] = True
                    else: 
                        queue.append((x+dx[i],y+dy[i],time+1,1))
                        visited[x+dx[i]][y+dy[i]] = True
                        brvisited[x+dx[i]][y+dy[i]] = True
        else:
            for i in range(4):
                if isInside(x+dx[i], y+dy[i]) and not brvisited[x+dx[i]][y+dy[i]] and box[x+dx[i]][y+dy[i]] == '0':
                        queue.append((x+dx[i],y+dy[i],time+1,1))
                        brvisited[x+dx[i]][y+dy[i]] = True
                        # box[x+dx[i]][y+dy[i]] = -1

bfs()
if ans != sys.maxsize:
    print(ans)
else:
    print(-1)