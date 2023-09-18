# stack
import sys
input = sys.stdin.readline
string = list(input().strip())
bomb = list(input().strip())
n = len(bomb)
stack = []

def explode():
    if len(stack)>= n and stack[-1*n:] == bomb:
        for _ in range(n):
            stack.pop()
        explode()

for i in string:
    stack.append(i)
    explode()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))