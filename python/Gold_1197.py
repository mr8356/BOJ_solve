# 최소 신장 트리 
heap = []
n, m = map(int, input().split())
for _ in range(m):
    heap.append(list(map(int, input().split())))

cnt = 0
weight = 0
nodes = [0] * (n+1)
for i in range(1,n+1):
    nodes[i] = i

def find(a):
    if nodes[a] ==a:
        return a
    else:
        nodes[a] = find(nodes[a])
        return nodes[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        if a<b:
            nodes[b] = a
        else:
            nodes[a] = b

heap.sort(key = lambda x : x[2])
i = 0
while cnt<n-1:
    w,a,b = heap[i][0] , heap[i][1], heap[i][2]
    if find(a) != find((b)):
        cnt += 1
        weight += w
        union(a, b)
    i+=1
print(weight)