#Stack
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int , input().split()))
stack = []
A = [-1]*n
stack.append(0)
for i in range(1,n):
    a = num[i]
    while len(stack)!=0:
        top = num[stack[-1]]
        if top < a:
            A[stack.pop()] = a
        else:
            break
    stack.append(i)
result = ""
for ch in A:
    result += str(ch) + ' '
print(result)

