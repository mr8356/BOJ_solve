import sys
input = sys.stdin.readline
tc = int(input())

def bellman():
  n,m,w = map(int, input().split())
  dist = [sys.maxsize] * (n+1)
  dist[1] = 0 #1 에서 출발한다고 가정
  edges = []
  # 경로 추가
  for _ in range(m):
    s,e,t = map(int, input().split())
    # 방향이 없는 경로
    edges.append((s,e,t))
    edges.append((e,s,t))
  # 웜홀 추가(방향있음)
  for _ in range(w):
    s,e,t = map(int, input().split())
    edges.append((s,e,t*-1))
  # N-1 번 경로 탐색 반복
  for _ in range(n-1):
    for s,e,t in edges:
      if dist[s] + t < dist[e]:
        dist[e] = dist[s] + t
  isCycle = False
  for s,e,t in edges:
      if dist[s] + t < dist[e]:
        isCycle = True
        break
  if isCycle:
    print("YES")
  else:
    print("NO")

for _ in range(tc):
  #  각 테스트 케이스 시작
  bellman()
  

