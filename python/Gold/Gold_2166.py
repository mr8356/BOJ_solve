n = int(input())
class Point:
  def __init__ (self,x,y):    #스택을 초기화
    self.x = x
    self.y = y

points = []
for i in range(n):
  x,y = map(int, input().split())
  p = Point(x,y)
  points.append(p)

a = 0
b = 0
for i in range(n):
  a += points[i].x * points[(i+1)%n].y
  b += points[(i+1)%n].x * points[i].y
print(format(abs((a-b)/2), ".1f"))