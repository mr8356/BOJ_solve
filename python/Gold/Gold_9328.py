#BFS
import sys
from collections import deque
input = sys.stdin.readline

# global variable
h,w = 0,0
box = []
keys = set()
visited = []

def isInside(n,m):
    if 0<=n<h:
        if 0<=m<w:
            return True
    return False

def findEntry():
  entries = []
  # h=0 , h-1
  for m in range(w):
    if box[0][m] != '*':
      entries.append((0,m))
    if box[h-1][m] != '*':
      entries.append((h-1,m))
  # side
  for n in range(1,h-1):
    if box[n][0] != '*':
      entries.append((n,0))
    if box[n][w-1] != '*':
      entries.append((n,w-1))
  return entries


def bfs():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    entries = findEntry()
    cnt = 0
    numOfDoors = 0
    for x,y in entries:
        if 'A' <= box[x][y] <= 'Z':
            numOfDoors+=1
    queue = deque(entries)
    repeat = 0
    while len(queue) != 0:
        # 한 사이클 종료 조건
        if len(queue) == numOfDoors:
            if repeat >= numOfDoors:
                return cnt
            repeat += 1
        n,m = queue.popleft()
        if 'a' <= box[n][m] <= 'z':
            keys.add(box[n][m])
        if 'A' <= box[n][m] <= 'Z':
            if (box[n][m].lower() in keys):
                numOfDoors -= 1
                repeat = 0
            else:
                queue.append((n,m))
                continue
        elif box[n][m] == '$':
            cnt+=1
            box[n][m] = '.'

        for i in range(4):
            if isInside(n+dx[i], m+dy[i]) and not visited[n+dx[i]][m+dy[i]]:
                ch = box[n+dx[i]][m+dy[i]]
                if ch == '.':
                    queue.append((n+dx[i],m+dy[i]))
                    visited[n+dx[i]][m+dy[i]] = True
                if 'a' <=ch<= 'z':
                    queue.append((n+dx[i],m+dy[i]))
                    keys.add(ch)
                    visited[n+dx[i]][m+dy[i]] = True
                if 'A' <= ch <= 'Z':
                        queue.append((n+dx[i],m+dy[i]))
                        visited[n+dx[i]][m+dy[i]] = True
                        numOfDoors += 1
                if ch == '$':
                    queue.append((n+dx[i],m+dy[i]))
                    visited[n+dx[i]][m+dy[i]] = True
    return cnt


t = int(input())
ans = []
for _ in range(t):
  h,w = map(int, input().split())
  box = []
  visited = [[False] * w for i in range(h)]
  for i in range(h):
    box.append(list(input()))
  keys = set(list(input()))
  ans.append(bfs())

for i in ans:
    print(i)