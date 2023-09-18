import sys
input = sys.stdin.readline
n,m = map(int, input().split())
inp = list(map(int,input().split()))
inp.sort()

def seq(start, nums, li):
  li.append(start)
  nums.remove(start)
  if len(li) == m:
    print(*li)
  for i in deduplicate(nums):
    seq(i,nums[::] ,li[::])

def deduplicate(li):
  if len(li)<2:
    return li
  prv = li[0]
  result = [prv]
  for i in range(1,len(li)):
    if prv == li[i]:
      continue
    else:
      prv = li[i]
      result.append(li[i])
  return result

for i in deduplicate(inp):
  seq(i,inp[::],[])