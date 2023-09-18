# 후위 표기식
inp = list(input())
stack = []
result = []
pri = {'*': 4, '/': 4, '+': 2, '-': 2, '(': 0, ')': 0}


def removeBracket():
    global stack
    while len(stack)>0:
        ch = stack.pop()
        if ch=='(':
            return
        result.append(ch)

for i in range(len(inp)):
    ch = inp[i]
    if ord('A') <= ord(ch) <= ord('Z'):
        result.append(ch)
    elif ch == ')':
        removeBracket()
    elif ch == '(':
        stack.append(ch)
    else:
        if len(stack) > 0 and pri[ch] <= pri[stack[-1]]:
            # 기존보다 우선순위 낮은얘오면 기존의 것을 차례대로 내보냄
            while len(stack) > 0 and pri[ch] <= pri[stack[-1]]:
                result.append(stack.pop())
        stack.append(ch)
while len(stack) > 0:
    result.append(stack.pop())

print(''.join(result))
# print(result)
# print(stack)
