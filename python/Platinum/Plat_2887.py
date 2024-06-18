import sys
input = sys.stdin.readline

n = int(input())
# 각 노드의 각 x,y,z좌표들을 따로 분류한 리스트
# (나중에 정렬해서 인접한 좌표끼리만 간선을 만들 예정)
xList = []
yList = []
zList = []
for i in range(n):
    x,y,z = map(int , input().split())
    xList.append((x, i)) # (_좌표, 노드번호)
    yList.append((y, i)) # (_좌표, 노드번호)
    zList.append((z, i)) # (_좌표, 노드번호)

edges = []
xList.sort()
yList.sort()
zList.sort()
for i in range(n-1):
    # 한좌표로 정렬 했을때 바로 옆에 있는 행성들끼리만 연결해서 간선 만듦
    # 0,1 1,2 ... n-1,n 짝짓기
    w = abs(xList[i][0] - xList[i+1][0]) # 가중치(거리)
    edges.append((w,xList[i][1], xList[i+1][1]))
    w = abs(yList[i][0] - yList[i+1][0]) # 가중치(거리)
    edges.append((w,yList[i][1], yList[i+1][1]))
    w = abs(zList[i][0] - zList[i+1][0]) # 가중치(거리)
    edges.append((w,zList[i][1], zList[i+1][1]))


edges.sort()
parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    i=0
    cnt=0
    distance=0
    while cnt < n-1:
        w,a,b = edges[i]
        i+=1
        if find(a) == find(b):
            continue
        cnt+=1
        distance+=w
        union(a,b)
    return distance

print(kruskal())