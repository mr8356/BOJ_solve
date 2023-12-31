# https://velog.io/@1998yuki0331/Python-%EB%B9%84%ED%8A%B8-%EB%A7%88%EC%8A%A4%ED%82%B9-%EC%A0%95%EB%A6%AC
import sys
input = sys.stdin.readline
S = 0 # 1~20 표현위해 0-21 index로 함
m = int(input())
for i in range(m):
  op = input().strip().split()
  try:
    op,num = op[0], op[1]
    num = int(num)
    if op == "add":
      S |= (1 << num)
    elif op == "remove":
      S &= ~(1 << num)
    elif op == "toggle":
      S ^= (1 << num)
    elif op == "check":
      print(1 if S&(1 << num) !=0 else 0)
  except:
    op = op[0]
    if op == "all":
      S = (1 << 21) - 1
    elif op == "empty":
      S = 0
