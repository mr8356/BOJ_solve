# 후위 표기식
inp = list(input())
stack = []
result = []
pri = {'*': 4, '/': 3, '+': 2, '-': 1,'(':0, ')':0}


def removeBracket():
    global stack
    for i in range(-1, -1*len(stack), -1):
        if stack[i] == '(':
            del stack[i]


for i in range(len(inp)):
    ch = inp[i]
    if ord('A') <= ord(ch) <= ord('Z'):
        result.append(ch)
    elif ch == ')':
        removeBracket()
    elif ch=='(':
        stack.append(ch)
    else:
        if len(stack) > 0:
            if pri[ch] > pri[stack[-1]]:
                stack.append(ch)
            else:
                # 기존보다 우선순위 낮은얘오면 기존의 것을 차례대로 내보냄
                while len(stack) > 0 and pri[ch] < pri[stack[-1]]:
                    result.append(stack.pop())
        else:
            stack.append(ch)
while len(stack) > 0:
    result.append(stack.pop())

print(''.join(result))
