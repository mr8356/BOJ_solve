# 유니온 파인드
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
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
    nodes[b_parent] = a_parent

for i in range(1,n+1):
    citys = list(map(int, input().split()))
    for j in range(n):
        if citys[j]==1:
            union(i , j+1)
route = list(map(int, input().split()))
check = True
route_parant = find(route[0])
for i in route:
    if find(i) != route_parant:
        check = False
        break
if check:
    print("YES")
else:
    print("NO")