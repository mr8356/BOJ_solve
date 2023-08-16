a,b,c = map(int, input().split())
#메모리제이션없는 탑-다운 : 재귀호출이 한개 밖에 없으므로 dp로 보기 힘들거같다.
n=a%c
def dac(t):
  if t==1:
    return n
  if t%2==0:
    return (dac(t//2)**2)%c
  else:
    return ((dac(t//2)**2)*n)%c
print(dac(b))

# DP문제라고 잘못생각해서 낸 오답들
# 아래 두 예시는 메모리제이션을 사용해서 메모리 초과가 났다.
#탑-다운 방식
# n = [0]*(b//2+1)
# n[1] = a%c
# def dac(t):
#   if t<=b//2 and n[t]!=0:
#     return n[t]
#   if t%2==0:
#     return (dac(t//2)**2)%c
#   else:
#     return ((dac(t//2)**2)*n[1])%c
# print(dac(b))

# 바텀-업 방식
# n = [1]*(b//2+1)
# n[1] = a%c
# for i in range(2,b//2+1):
#   if i%2==0:
#     n[i] = (n[i//2]**2)%c
#   else:
#     n[i] = (n[i-1]*n[1])%c;
# if b%2==0:
#   print((n[b//2]**2)%c);
# else:
#   print(((n[b//2]**2)*n[1])%c)