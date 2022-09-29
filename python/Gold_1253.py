# two pointer
import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int , input().split()))
num.sort()
cnt =0
for i in range(n):
    goal = num[i]
    i_index = 0
    j_index = n-1
    while i_index<j_index:
        sum = num[i_index] + num[j_index]
        if sum < goal:
            i_index+=1
        elif sum > goal:
            j_index-=1
        else:
            if i_index!=i and j_index!=i :
                cnt+=1
                break
            if i_index == i:
                i_index+=1
            elif j_index == i:
                j_index-=1
print(cnt)
