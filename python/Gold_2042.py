# 세그먼트 트리
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
x = 0
while 2**x < n:
    x+=1
tree = [0] * (2**(x+1)+1)
for i in range(2**x, 2**x+n):
    tree[i] = int(input())
#make tree
for i in range(2**x-1,0,-1):
    tree[i] = tree[i*2] + tree[i*2+1]

def getSum(start , end):
    nums = []
    start = 2**x -1 + start
    end = 2**x -1 + end
    while start<=end:
        if start%2==1:
            nums.append(tree[start])
        if end%2==0:
            nums.append(tree[end])
        start = (start+1)//2
        end = (end-1)//2
    return sum(nums)

def setNode(node , number):
    node = 2**x -1 + node
    diff = number - tree[node]
    while node>0:
        tree[node] += diff
        node//=2

for _ in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        setNode(b,c)
    else:
        print(getSum(b,c))