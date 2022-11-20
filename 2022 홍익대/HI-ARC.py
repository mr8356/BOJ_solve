import sys
input = sys.stdin.readline
n = int(input())
s = input().strip()
# H I A R C
# 0 1 2 3 4
hiarc = [0,0,0,0,0]
for c in s:
    if c == 'H':
        hiarc[0] += 1
    elif c=='I':
        hiarc[1] +=1
    elif c=='A':
        hiarc[2] +=1
    elif c=='R':
        hiarc[3] +=1
    elif c=='C':
        hiarc[4] +=1
print(min(hiarc))
    