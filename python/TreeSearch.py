# 이진 트리
# 딕셔너리로 트리 표현!!!!!
# 1991
import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
tree = {}
# 트리 제작
for i in range(0,n):
    re = list(input().split())
    tree[re[0]] = [re[1] , re[2]]

#전위순회 // (루트) (왼쪽 자식) (오른쪽 자식)
def preOrder(node_ch):
    if node_ch == '.':
        return
    print(node_ch)
    for i in tree[node_ch]:
        preOrder(i)

#중위순회 // (왼쪽 자식) (루트) (오른쪽 자식)
def inOrder(node_ch):
    if node_ch == '.':
        return
    inOrder(tree[node_ch][0])
    print(node_ch)
    inOrder(tree[node_ch][1])

#후위순회 // (왼쪽 자식) (오른쪽 자식) (루트)
def postOrder(node_ch):
    if node_ch == '.':
        return
    postOrder(tree[node_ch][0])
    postOrder(tree[node_ch][1])
    print(node_ch)

    
preOrder('A')
print('\n')
inOrder('A')
print('\n')
postOrder('A')