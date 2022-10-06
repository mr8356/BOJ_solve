# 유니온 파인드
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
nodes = [0]*(n+1)
for i in range(n+1):
    nodes[i] = i

def find(a):
    if a == nodes[a]:
        return a
    else :
        nodes[a] = find(nodes[a])
        return nodes[a]

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        nodes[b_parent] = a_parent

for i in range(m):
    proc, a, b = map(int, input().split())
    if proc == 0:
        union(a, b)
    else :
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
