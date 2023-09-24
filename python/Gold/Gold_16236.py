from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]

shark = ()
level = 2
eatCount = 0

for i in range(n):
    for j in range(n):
        if box[i][j] == 9:
            shark = (i, j)
            box[i][j] = 0


def isInside(x, y):
    if 0 <= x < n:
        if 0 <= y < n:
            return True
    return False


def bfs():
    global shark, box, level, eatCount
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    sx, sy = shark
    queue.append((sx, sy, 0))
    visited[sx][sy] = True
    dy = [1, 0, 0, -1]
    dx = [0, -1, 1, 0]
    fish_x = n
    fish_t = n*n
    # 물고기들의 y값들을 저장(어차피 x,t가 같은 물고기만 모집함)
    fish = []
    while queue:
        x, y, t = queue.popleft()
        # 발견했었던 물고기의 시간보다 초과했으면 중단
        # t가 동일한 여러 물고기를 저장하는 것이 목적
        if t>=fish_t:
          break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and not visited[nx][ny]:
                if box[nx][ny] == 0 or box[nx][ny] == level:
                    queue.append((nx, ny, t+1))
                    visited[nx][ny] = True
                elif box[nx][ny] < level:
                    visited[nx][ny] = True
                    # 가까운(t가 작은) 물고기가 여러마리면 위에 있는(x가 작은) 물고기 채택
                    if nx<=fish_x:
                      fish.append(ny)
                      fish_x, fish_t = nx, t+1
    # 잡을수 있는 물고기가 없음
    if len(fish)==0:
      return -1
    # 위에있고 가까운 물고기중 가장 왼쪽(y가 작음)물고기 구하기
    fish_y = min(fish)
    box[fish_x][fish_y] = 0
    eatCount += 1
    if eatCount == level:
        level += 1
        eatCount = 0
    shark = (fish_x,fish_y)
    # 걸린 시간 반환 
    return fish_t

time = 0
while True:
    result = bfs()
    if result == -1:
        break
    time += result

print(time)
