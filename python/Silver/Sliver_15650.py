n,m = map(int, input().split())

def seq(start, li):
  li.append(start)
  if len(li) == m:
    print(*li)
  for i in range(start+1,n+1):
    seq(i, li[::])

for i in range(1,n+1):
  seq(i,[])