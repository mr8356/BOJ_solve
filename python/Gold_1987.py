import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
box = []
for i in range(n):
    # 받는 문자들을 아스키코드로 변환하고 인덱스로 활용하기 위해
    # 아스키코드-A 적용. ex) A = 0, B = 2, C = 3
    box.append(list(map(lambda x: ord(x)-ord('A'), list(input()))))


def isInside(x, y):
    if 0 <= x < n:
        if 0 <= y < m:
            return True
    return False


maxDepth = 1


def dfs(x, y, visted, depth):
    global box, maxDepth
    if depth > maxDepth:
        maxDepth = depth
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if isInside(nx, ny):
            if not visted[box[nx][ny]]:
                tmp = visted.copy()
                tmp[box[nx][ny]] = True
                dfs(nx, ny, tmp, depth+1)


visted = [False]*(ord('Z')-ord('A')+1)
visted[box[0][0]] = True
dfs(0, 0, visted, 1)
print(maxDepth)


# 1st
# import sys
# from collections import deque
# input = sys.stdin.readline
# r,c = map(int, input().split())
# maps = [list(input().strip()) for _ in range(r)]
# move = [(-1,0),(1,0),(0,-1),(0,1)]
# q = set()
# q.add((0,0,maps[0][0]))
# answer = 0
# def bfs(q):
#   global answer
#   while q:
#     a,b,alpha = q.pop()
#     answer = max(answer, len(alpha))
#     if answer == 26:
#       return
#     for move_x, move_y in move:
#       nx = a + move_x
#       ny = b + move_y
#       if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alpha:
#         q.add((nx,ny,alpha + maps[nx][ny]))
#   return
# bfs(q)
# print(answer)


# 2st
# R, C = map(int, input().split())
# board = [list(input()) for _ in range(R)]

# visited = [[''] * C for _ in range(R)]
# Di = [-1, 1, 0, 0]
# Dj = [0, 0, -1, 1]
# result = 0
# stack = [(0, 0, 1, board[0][0])]

# while stack:
#     i, j, deep, words = stack.pop()
#     if deep > result:
#         result = deep
#         if result == 26:
#             break

#     for k in range(4):
#         ni, nj = i + Di[k], j + Dj[k]

#         if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in words:
#             temp = words + board[ni][nj]
#             if temp not in visited[ni][nj]:
#                 visited[ni][nj] = temp
#                 stack.append((ni, nj, deep + 1, temp))
# print(result)
