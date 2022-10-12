import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k = 0
while 2**k < n:
    k+=1
tree = [sys.maxsize] * (2**(k+1)+1)
for i in range(2**k , 2**k+n):
    tree[i] = int(input())
#mk tree
for i in range(2**k-1 ,0,-1):
    tree[i] = min(tree[i*2] , tree[i*2+1])

def getMin(start , end):
    start = 2**k -1 + start
    end = 2**k -1 + end
    nums = []
    while start<=end:
        if start%2==1:
            nums.append(tree[start])
        if end%2 == 0:
            nums.append(tree[end])
        start = (start+1)//2
        end = (end-1) //2
    return min(nums)

for _ in range(m):
    a,b = map(int,input().split())
    print(getMin(a, b))