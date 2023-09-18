#Stack
import sys
input = sys.stdin.readline
num_of_lines = int(input())
for i in range(num_of_lines):
    in_line = input().strip()
    stack = []
    isVailed = True
    for ch in in_line:
        if ch=='(':
            stack.append(ch)
        else:
            if len(stack) ==0:
                isVailed = False
                break
            else:
                stack.pop()
    if isVailed and len(stack)==0:
        print("YES")
    else:
        print("NO")