# 지금까지 틀린이유 : 2차원배열처럼 변형 객체 같은 경우 copy(), [::]와 같은 얕은복사론 안된다
# 얕은 복사는 일반 리스트 까지 되고, 더 복잡한 형태는 지원 안한다.
# 깊은 복사를 해야되므로 copy.deepcopy(원본) 를 적용한다.
# deecopy 방법 :
# test_box = copy.deepcopy(box)
# python3 기준 3000ms
#
# 또는 2차원 배열을 슬라이싱해서 얕은 복사가 가능한 1차원 배열로 나워서 다시 붙여서 만들어준다.
# deepcopy 방식보다 슬라이싱해서 다시 붙이는게 빠르다
# 슬라이싱 방법 :
# test_box = []
#     for b in box:
#         test_box.append(b.copy())
# python3 기준 2000ms


from collections import deque
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
# print(box)
air, wall, virus = 0, 1, 2


air_cnt = -3
virus_point = []
for i in range(n):
    for j in range(m):
        if box[i][j] == air:
            air_cnt += 1
        if box[i][j] == virus:
            virus_point.append((i, j))
            box[i][j] = 4


def isInside(x, y):
    if 0 <= x < n:
        if 0 <= y < m:
            return True
    return False


def bfs(x1, y1, x2, y2, x3, y3):
    global air_cnt, virus_point
    test_box = []
    for b in box:
        test_box.append(b.copy())
    test_box[x1][y1] = wall
    test_box[x2][y2] = wall
    test_box[x3][y3] = wall
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque(virus_point)
    virus_cnt = -1 * len(virus_point)
    while queue:
        x, y = queue.popleft()
        if test_box[x][y] == virus:
            continue
        test_box[x][y] = virus
        virus_cnt += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and test_box[nx][ny] == air:
                queue.append((nx, ny))
    safezone = air_cnt - virus_cnt
    return safezone


max_safezone = 0

for i in range(n):
    for j in range(m):
        if box[i][j] != air:
            continue
        for x in range(i, n):
            for y in range(m):
                if x == i and y <= j:
                    continue
                if box[x][y] != air:
                    continue
                for a in range(x, n):
                    for b in range(m):
                        if a == x and b <= y:
                            continue
                        if box[a][b] != air:
                            continue
                        max_safezone = max(max_safezone, bfs(i, j, x, y, a, b))
print(max_safezone)
