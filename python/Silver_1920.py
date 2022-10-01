# 이진 탐색
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
requests = list(map(int, input().split()))
numbers.sort()

for find in requests:
    low_index = 0
    high_index = n-1
    exist = False
    while low_index <= high_index:
        mid_index = int((low_index + high_index)/2)
        if numbers[mid_index] == find:
            exist = True
            break
        elif numbers[mid_index] < find:
            low_index = mid_index+1
        else:
            high_index = mid_index-1
    if exist:
        print(1)
    else:
        print(0)
            
        