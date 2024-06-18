from collections import Counter
lines = []
n = int(input())
parent = [i for i in range(n)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b: # 작은 쪽을 부모로 통일
        parent[b] = a
    else:
        parent[a] = b

for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    lines.append(((x1,y1),(x2,y2)))

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    result = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0

def isSegment(p1,p2,p3):
    x1, x2 = min(p1[0], p2[0]), max(p1[0],p2[0])
    y1, y2 = min(p1[1], p2[1]), max(p1[1],p2[1])
    if x1<=p3[0]<=x2 and y1<=p3[1]<=y2:
        return True
    else:
        return False


def isCross(line1, line2):
    p1, p2, p3, p4 = line1[0], line1[1], line2[0], line2[1]
    a,b,c,d = ccw(p1,p2,p3), ccw(p1,p2,p4),ccw(p3,p4,p1), ccw(p3,p4,p2)
    if a*b<0 and c*d<0:
        return True
    if a==0 and isSegment(p1,p2,p3):
        return True
    elif b==0 and isSegment(p1,p2,p4):
        return True
    elif c==0 and isSegment(p3,p4,p1):
        return True
    elif d==0 and isSegment(p3,p4,p2):
        return True
    return False

for i in range(n-1):
    for j in range(i+1,n):
        if find(i) == find(j):
            continue
        else:
            if isCross(lines[i],lines[j]):
                union(i,j)

for i in range(n):
    find(i)


cnt = Counter(parent)

print(len(cnt))
print(cnt.most_common()[0][1])