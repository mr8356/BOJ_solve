import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 전위순위 결과라 루트/왼/오른 형식으로 돼있음
tree = []
while True:
  try:
    tree.append(int(input()))
  except:
    break


# 재귀할때마다 부분트리나 리스트를 주고 받으면 시간이 오래걸리니까
# '구간'을 주고 받는다. 시작 인덱스, 끝 인덱스
def postorder(s,e):
  root = tree[s]
  if s==e:
    print(root)
    return
  # 오른쪽 노드의 시작. mid가 안나오면 오른쪽 노드가 없음.
  mid = 0
  # 루트를 제외한 s+1 ~ e 탐색
  for i in range(s+1,e+1):
    # 루트보다 큰게 나오면 그게 오른쪽 부분트리의 시작 (mid)
    if tree[i] > root:
      mid = i
      break
  # 왼쪽 노드 탐색
  if mid!=s+1:
    if mid == 0:
      postorder(s+1,e)
    else:
      postorder(s+1,mid-1)
  # 오른쪽 노드 탐색
  if mid!=0:
    postorder(mid,e)
  # 루트 탐색(하나)
  print(root)

postorder(0, len(tree)-1)