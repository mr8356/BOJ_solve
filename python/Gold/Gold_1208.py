import sys
from itertools import combinations, permutations
from collections import Counter

input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
middleIdx = n//2


def makeSubSums(seq):
    result = []
    for i in range(1, len(seq)+1):
        combi = list(combinations(seq, i))
        for c in combi:
            result.append(sum(c))
    return result


leftSums = makeSubSums(nums[:middleIdx])
rightSums = makeSubSums(nums[middleIdx:])

leftSums.append(0)
rightSums.append(0)
leftSums.sort()
rightSums.sort()

# 각 원소별 횟수를 딕셔너리 형태로 저장
rightConter = Counter(rightSums)

result = 0
for sub in leftSums:
    find = s - sub
    if find in rightConter:
        result += rightConter[find]
if s == 0:
    result -= 1

print(result)
