import sys
input = sys.stdin.readline
n,m = map(int, input().split())
numSet = set(list(map(int, input().split())))
nums = list(numSet)
nums.sort()
size = len(nums)

def choose(prv, li):
  global nums, m
  if len(li)==m:
    print(' '.join(li))
    return
  idx = nums.index(prv)
  for num in nums[idx::]:
    tmp = li[::]
    tmp.append(str(num))
    choose(num,tmp)

choose(nums[0],[])
