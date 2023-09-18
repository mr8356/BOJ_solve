#Bubble Sort
import sys
input = sys.stdin.readline
n = int(input())
num = []
for i in range(n):
    #첫번째 정렬기준: input 숫자 자체로 정렬
    #두번째: 인덱스 번호(순서) => 나중에 호출할 예정
    num.append( (int(input()) , i) )

num.sort() # (값 오름차순 , 값의 순서) 튜플

Max = 0
for i in range(n):
    # num[i][0] 는 값 , i는 오름차순(정렬된)순서
    Max = max(Max, num[i][1] - i)
    # 정렬된 순서 - 원래 순서 > 0 : 왼쪽으로 이동
    # 왼쪽으로 루프마다 1칸만 이동가능
print(Max+1)
# 4 - 1
#