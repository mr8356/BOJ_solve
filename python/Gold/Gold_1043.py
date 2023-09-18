# 1043 Liar
# union find
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
peoples = [0]*(n+1)  # union list
for i in range(1, n+1):
    peoples[i] = i


def find(a):
    if peoples[a] == a:
        return a
    else:
        peoples[a] = find(peoples[a])
        return peoples[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        peoples[b] = a


knowers = list(map(int, input().split()))[1::]
if len(knowers) == 0:
    print(m)
    exit()

first_knower = knowers[0]

for k in knowers[1::]:
    union(first_knower, k)

partys = [True]*(m)  # True is available party
first_teamates = []
for i in range(m):
    teams = (list(map(int, input().split()))[1::])
    first_teamates.append(teams[0])
    for k in teams[1::]:
        union(first_teamates[i], k)

cnt = 0
for i in range(m):
    if find(first_teamates[i]) == find(first_knower):
        continue
    else:
        cnt += 1

print(cnt)
