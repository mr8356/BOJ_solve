from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

cleanerIdxs = []
for i in range(n):
    for j in range(m):
        if box[i][j] == -1:
            cleanerIdxs.append(i)


def isInside(x, y):
    if 0 <= x < n:
        if 0 <= y < m:
            return True
    return False


def spread():
    # 확산
    global box
    nodes = []
    for i in range(n):
        for j in range(m):
            if box[i][j] >= 5:
                nodes.append((i, j, box[i][j]))
    for x, y, dust in nodes:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and (box[nx][ny] != -1):
                box[nx][ny] += dust//5
                cnt += 1
        box[x][y] -= (dust//5) * cnt


def moveDust():
    global box
    new_box = []
    new_box.append(box[0][1:m]+[box[1][m-1]])
    # print(box[0][1:m]+[box[1][m-1]])
    for i in range(1, cleanerIdxs[0]):
        new_box.append([box[i-1][0]]+box[i][1:m-1]+[box[i+1][m-1]])
    for i in range(cleanerIdxs[0], cleanerIdxs[1]+1):
        new_box.append([-1, 0]+box[i][1:m-1])
    for i in range(cleanerIdxs[1]+1, n-1):
        new_box.append([box[i+1][0]]+box[i][1:m-1]+[box[i-1][m-1]])
    new_box.append(box[n-1][1:m]+[box[n-2][m-1]])
    box = new_box


for _ in range(t):
    spread()
    moveDust()

totalDust = 2  # -1 두개
for row in box:
    totalDust += sum(row)

print(totalDust)
