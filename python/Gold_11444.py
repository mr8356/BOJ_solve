# 피보나치 수 - 도가뉴 항등식
# a(2n-1)**2 = a(n)**2 + a(n-1)**2
# a(2n) = a(n)[a(n) + 2*a(n-1)]
n = int(input())
DP = {}
DP[1] = 1
DP[2] = 1
DP[3] = 2
def fibo(num):
  if num in DP:
    return DP[num]
  if num%2==1:
    m = (num+1)//2
    DP[num] = (fibo(m)**2 + fibo(m-1)**2)%1000000007
    return DP[num]
  else:
    an = fibo(num//2)
    an1 = fibo(num//2-1)
    DP[num] = (an**2 + 2*an*an1)%1000000007
    return DP[num]
fibo(n)
print(DP[n])