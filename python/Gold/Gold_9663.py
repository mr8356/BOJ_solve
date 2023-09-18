n = int(input())
cnt = 0
row = [0]*(n+1)

def isValid(r):
  for i in range(1,r):
    if abs(r-i)==abs(row[r]-row[i]) or row[i]==row[r]:
      return False
  return True

def queen(r):
  global row,cnt
  if r==n+1:
        cnt+=1
        return
  for x in range(1,n+1):
    row[r] = x
    if isValid(r):
      queen(r+1)
  #적합한게 없으면 여기서 끊김

#덮어씌우고, 자신의 이전 행만 검사하므로 row초기화 할 필요가 없음

queen(1)
print(cnt)