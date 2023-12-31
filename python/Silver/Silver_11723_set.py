import sys
input = sys.stdin.readline
S = set()
allSet = set([i for i in range(1, 21)])
m = int(input())
for i in range(m):
  op = input().strip().split()
  try:
    op,num = op[0], op[1]
    num = int(num)
    if op == "add":
      S.add(num)
    elif op == "remove":
      S.discard(num)
    elif op == "toggle":
      if num in S:
        S.discard(num)
      else:
        S.add(num)
    elif op == "check":
      print(1 if num in S else 0)
  except:
    op = op[0]
    if op == "all":
      S = allSet.copy()
    elif op == "empty":
      S = set()
