#DP
#UNDOOO!!!
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
D = [0] * (n)
P = [0] * (n)
P[0] = A[0]
rem = -1
if A[0]>0:
    D[0] = A[0]
else:
    D[0] = 0
    rem = 0

for i in range(1,n):
    P[i] = P[i-1] + A[i]
    if A[i] > 0:
        D[i] = D[i-1] + A[i]
    else:
        if rem == -1:
            rem = i
            D[i] = D[i-1]
        else:#삭제를 이미 했을때
            temp = rem
            if P[i-1]-P[rem] > D[i-1] + A[rem]:
                D[i]= P[i-1]-P[rem]
                rem = i
            else:
                D[i] = D[i-1] + A[rem]
                rem = i
            if D[i] < D[i-1] + A[i]:
                D[i] = D[i-1] + A[i]
                rem  = temp
print(max(D))





# i 번쨰가 음수 일때 요령 (i번째 무조건 있어야됨)
# 삭제 아직 안했을때 => 자신을 삭제 (rem = 자신인덱스로)

#삭제를 이미 했을때
# 자신을 삭제 => 뒷쪽은 부활하므로(rem = 자신인덱스로) 1. 음수 기준으로 끊거나 2.그냥 다 더함
# 뒷쪽을 채택 => 자신을 삭제 못하니 그래도 더함 (rem 변화없음)

