import sys
from collections import deque
input = sys.stdin.readline
n , m = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int,input().split())))

queue = deque()

def isInside(x,y):
    if 0<=x<n:
        if 0<=y<m:
            return True
    return False

for x in range(n):
    for y in range(m):
        cnt = 0
        if box[x][y] == 0:
            continue
        if isInside(x-1, y) and box[x-1][y] == 0:
            cnt+=1
        if isInside(x+1, y) and box[x+1][y] ==0:
            cnt+=1
        if isInside(x, y+1) and box[x][y+1]==0:
            cnt+=1
        if isInside(x, y-1) and box[x][y-1]==0:
            cnt+=1
        if cnt>=2:
            box[x][y] = -1 # 임시
            queue.append((x,y,1))#x,y,소멸되는데 걸리는 시간
        elif cnt ==1:
            box[x][y] = 2


def bfs():
    totalTime = 0
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        time = node[2]
        totalTime = max(totalTime, time)
        box[x][y] = 0
        if isInside(x-1, y) :
            if box[x-1][y] == 1:
                box[x-1][y] +=1
            elif box[x-1][y] == 2:
                queue.append((x-1,y, time+1))
                box[x-1][y] = 0
        if isInside(x+1, y):
            if box[x+1][y] == 1:
                box[x+1][y] +=1
            elif box[x+1][y] == 2:
                queue.append((x+1,y, time+1))
                box[x+1][y] = 0
        if isInside(x, y+1):
            if box[x][y+1] == 1:
                box[x][y+1] +=1
            elif box[x][y+1] == 2:
                queue.append((x,y+1, time+1))
                box[x][y+1] = 0
        if isInside(x, y-1):
            if box[x][y-1] == 1:
                box[x][y-1] +=1
            elif box[x][y-1] == 2:
                queue.append((x,y-1, time+1))
                box[x][y-1] = 0
    return totalTime
        
print(bfs())