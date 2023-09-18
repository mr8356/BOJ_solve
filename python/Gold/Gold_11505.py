# 세그먼트 트리
n, m, k = map(int, input().split())
x = 0
while n>2**x:
    x+=1
tree = [1]*(2**(x+1)+1)
for i in range(2**x,2**x+n):
    tree[i] = int(input())
# make tree
for i in range(2**x-1 , 0, -1):
    tree[i] = (tree[i*2] * tree[i*2+1])%1000000007

def changeVal(index , val):
    index = 2**x-1+index
    tree[index] = val
    index//=2
    while index>0:
        tree[index] = (tree[index*2] * tree[index*2 +1])%1000000007
        index//=2

def getMult(start , end):
    start = 2**x -1 + start
    end = 2**x -1 + end
    result = 1
    while start<=end:
        if start%2==1:
            result*=tree[start]
            result%=1000000007
        if end%2==0:
            result*=tree[end]
            result%=1000000007
        start = (start+1)//2
        end = (end-1)//2
    return result
ans = ""
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        changeVal(b, c)
    else:
        ans+=(str(getMult(b, c))+"\n")
print(ans)
    