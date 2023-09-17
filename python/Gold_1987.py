import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
box = [list(input()) for _ in range(n)]
# 똑같은 곳을 다시 가는 경우를 최대한 빼기위해 visted는 항상 필요
# 아무리 지난 알파벳으로 검증한다고 해도 똑같은 알파벳 조건으로 다시오는 경우가 있음
visited = [[''] * m for _ in range(n)]

def isInside(x, y):
    if 0 <= x < n:
        if 0 <= y < m:
            return True
    return False


maxDepth = 1

def dfs(x, y, depth, prv):
    global box, maxDepth
    if depth > maxDepth:
        maxDepth = depth
        if maxDepth == 26:
            print(maxDepth)
            exit()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if isInside(nx, ny):
            char = box[nx][ny]
            # 1.입장해도 되는 지(새알파벳인지) and 2.이전에 똑같은 조건으로 입장한건 아닌지(중복 발생)
            if char not in prv and not prv + char == visited[nx][ny]:
                visited[nx][ny] = prv + char
                dfs(nx, ny, depth+1, visited[nx][ny])


visited[0][0] = box[0][0]
dfs(0, 0, 1, box[0][0])


print(maxDepth)
