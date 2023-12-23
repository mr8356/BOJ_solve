from heapq import heappush, heappop
import sys
input = sys.stdin.readline
queue = []
jewels = []
n, k = map(int, input().split())
bags = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))
for _ in range(k):
    bags.append(int(input()))

# 가방 크기, 보석 크기 오름차순(작->큰)
bags.sort()
jewels.sort()

# 훔칠수 있는 보석들의 리스트 (무게 고려 함)
steal_able_heap = []

result = 0
for bag in bags:
    while jewels:
        # 가방이 크거나 같으면 steal_able_heap에 넣는다
        # 가장 작은 값부터 탐색 (idx 0)
        if bag>=jewels[0][0]:
            # 가격 저장
            heappush(steal_able_heap, -1 * jewels[0][1])
            heappop(jewels)
        else:
            break
    if steal_able_heap:
        # 지금까지 훔칠수 있느 것에 가장 v가 큰 값을 훔침
        # 힙에 남아 있는 건 어차피 다음 가방들(무게가 더 큰)도 담을수 있는 것이므로 남겨두고 씀
        value = heappop(steal_able_heap)
        result-=value
print(result)