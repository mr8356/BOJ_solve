#two point
import sys
n = int(input())
start, end, cnt , sum = 1,1,1,1
while end < n:
    if sum<n :
        end+=1
        sum+=end
    elif sum==n :
        cnt+=1
        end+=1
        sum+=end
    else:
        sum-=start
        start+=1
print(cnt)