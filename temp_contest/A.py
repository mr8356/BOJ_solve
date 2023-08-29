# 보물 지도 PyPy3로 제출
n = int(input())
x1 = 1000000001
x2 = -1000000001
y1 = 1000000001
y2 = -1000000001
if n<4:
  print("Infinity")
  exit()
else:
  for i in range(n):
    x,y,p = list(input().split())
    if p=='L':
      x1 = min(int(x), x1)
    elif p=='R':
      x2 = max(int(x), x2)
    elif p=='D':
      y1 = min(int(y), y1)
    else:
      y2 = max(int(y), y2)
if x1 == 1000000001 or y1 == 1000000001 or x2 == -1000000001 or y2 == -1000000001:
  print("Infinity")
else:
  print((x1-x2-1)*(y1-y2-1))