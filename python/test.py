n,m = 3,3
box = [[1,1,0],[0,0,1],[1,1,0]]
air = 0

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
                        print(i, j, x, y, a, b)
