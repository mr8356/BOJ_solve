import sys
from collections import deque
input = sys.stdin.readline
n , m = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
box = []
for i in range(n):
    box.append(list(map(lambda x:'c' if x==1 else x,list(map(int,input().split())))))

cheeseQueue = deque()

def isInside(x,y):
    if 0<=x<n:
        if 0<=y<m:
            return True
    return False

def printBox():
    global box
    for i in range(n):
        print(*box[i])
    print()

def isMelt():
    for i in range(n):
        for j in range(m):
            if box[i][j]=='c' or box[i][j]==1:
                return False
    return True

def initBfs():
    global cheeseQueue
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx,ny):
                if box[nx][ny] == 'c':
                    box[nx][ny] = 1
                elif box[nx][ny]==1:
                    box[nx][ny]= 'a'
                    cheeseQueue.append((nx,ny))
                elif box[nx][ny] == 0:
                    queue.append((nx,ny))
                    box[nx][ny] = 'a' # air

def bfs():
    global cheeseQueue
    queue = cheeseQueue.copy()
    cheeseQueue = deque()
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx,ny):
                if box[nx][ny] == 'c':
                    box[nx][ny] = 1
                elif box[nx][ny]==1:
                    box[nx][ny]= 'a'
                    cheeseQueue.append((nx,ny))
                elif box[nx][ny] == 0:
                    queue.append((nx,ny))
                    box[nx][ny]= 'a'

initBfs()
time = 1
while not isMelt():
    bfs()
    time+=1

print(time)