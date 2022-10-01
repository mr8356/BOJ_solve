#Priority Queue
from queue import PriorityQueue
import sys
input = sys.stdin.readline
n = int(input())
# 우선 순위 큐 선언
absQueue = PriorityQueue()
for _ in range(n):
    request = int(input())
    if request == 0:
        if absQueue.empty():
            print(0)
        else:
            value = absQueue.get()[1]
            print(value)
    else:
        # 첫번째 우선순위: 절댓값 , 두번째 우선순위: 값(음수 우선)
        absQueue.put( (abs(request) , request) ) # 튜플!