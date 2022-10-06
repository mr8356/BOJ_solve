# 1043 Liar
# union find
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
peoples = [0]*(n+1) # union list
for i in range(1,n+1):
    peoples[i] = i
knower_input = list(map(int, input().split()))
knowers = knower_input[1:-1]

def find(a):
    if peoples[a] == a:
        return a
    else:
        peoples[a] = find(peoples[a])
        return peoples[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        peoples[b] = a
partys = [True]*(m) # True is available party
teams = [[]]
for i in range(m):
    teams.append(list(map(int, input().split()))[1:-1])
    for j in knowers:
        if j in teams[0]:
            partys[i] = False
            for k in teams[0]:
                union(j , k)
            break
for i in range(m):
    if partys[i] == False:
        continue
    team = teams[i]
    for man in team:
        if find(man) in knowers:
            partys[i] = False
            break
cnt =0 
for party in partys:
    if party:
        cnt+=1
print(cnt)