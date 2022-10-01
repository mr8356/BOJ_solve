# 이분(매개변수) 탐색
import sys
input = sys.stdin.readline
n ,m = map(int , input().split())
classes = list(map(int, input().split()))
# main => size of one blue ray
# lesser the better
low = max(classes)
high = sum(classes)

def isValid(size):
    sum = 0
    cnt = 0
    for i in classes:
        if sum+i <= size:
            sum+=i
        else:
            cnt+=1
            sum = i
    if cnt!=0:
        cnt+=1
    if cnt>m:
        return False
    else:
        return True

#size big is ok. but smaller is good
#size small is not ok
result = high
while low<=high:
    mid = int((low+high)/2)
    if isValid(mid):
        result = mid
        high = mid-1
    else:#too small
        low = mid+1
print(result)