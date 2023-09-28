import sys
input = sys.stdin.readline

x = 1000000007
m = int(input())

def dac(a, b):
  if b == 1:
    return a%x
  elif b%2==0:
    return (dac(a, b//2)**2)%x
  else:
    return ((dac(a,b//2)**2) * a)%x
    
result = 0
for i in range(m):
  n,s = map(int, input().split())
  result += (s * dac(n,x-2)) % x
  result %= x

print(result)
