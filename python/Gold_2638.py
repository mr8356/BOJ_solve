import sys
from collections import deque
input = sys.stdin.readline
n , m = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(lambda x:'c' if x==1 else x,list(map(int,input().split())))))

queue = deque()
cheeseQueue = deque()

def isInside(x,y):
    if 0<=x<n:
        if 0<=y<m:
            return True
    return False

def initBfs(node):
    global queue,cheeseQueue
    x,y = node
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if isInside(x-1, y) :
            if box[x-1][y] == 'c':
                box[x-1][y] = 1
            elif box[x-1][y]==1:
                cheeseQueue.append((x-1,y,1))
            elif box[x-1][y] == 0:
                queue.append((x-1,y))
                box[x-1][y] = 'a' # air
        if isInside(x+1, y):
            if box[x+1][y] == 'c':
                box[x+1][y] = 1
            elif box[x+1][y]==1:
                cheeseQueue.append((x+1,y,1))
            elif box[x+1][y] == 0:
                queue.append((x+1,y))
                box[x+1][y] = 'a'
        if isInside(x, y+1):
            if box[x][y+1] == 'c':
                box[x][y+1] = 1
            elif box[x][y+1]==1:
                cheeseQueue.append((x,y+1,1))
            elif box[x][y+1] == 0:
                queue.append((x,y+1))
                box[x][y+1] = 'a'
        if isInside(x, y-1):
            if box[x][y-1] == 'c':
                box[x][y-1] = 1
            elif box[x][y-1]==1:
                cheeseQueue.append((x,y-1,1))
            elif box[x][y-1] == 0:
                queue.append((x,y-1))
                box[x][y-1] = 'a'

def bfs():
    global cheeseQueue
    totalTime = 0
    while cheeseQueue:
        x,y,time = cheeseQueue.popleft()
        totalTime = max(totalTime, time)
        if isInside(x-1, y) :
            if box[x-1][y] == 'c':
                box[x-1][y] = 1
            elif box[x-1][y]==1:
                cheeseQueue.append((x-1,y,time+1))
                box[x-1][y] = 'a'
            elif box[x-1][y] == 0:
                initBfs((x-1,y))
                box[x-1][y] = 'a' # air
        if isInside(x+1, y):
            if box[x+1][y] == 'c':
                box[x+1][y] = 1
            elif box[x+1][y]==1:
                cheeseQueue.append((x+1,y,time+1))
                box[x+1][y] = 'a'
            elif box[x+1][y] == 0:
                initBfs((x+1,y))
                box[x+1][y] = 'a'
        if isInside(x, y+1):
            if box[x][y+1] == 'c':
                box[x][y+1] = 1
            elif box[x][y+1]==1:
                cheeseQueue.append((x,y+1,time+1))
                box[x][y+1] = 'a'
            elif box[x][y+1] == 0:
                initBfs((x,y+1))
                box[x][y+1] = 'a'
        if isInside(x, y-1):
            if box[x][y-1] == 'c':
                box[x][y-1] = 1
            elif box[x][y-1]==1:
                cheeseQueue.append((x,y-1,time+1))
                box[x][y-1] = 'a'
            elif box[x][y-1] == 0:
                initBfs((x,y-1))
                box[x][y-1] = 'a'
    return totalTime

initBfs((0,0))
print(bfs())