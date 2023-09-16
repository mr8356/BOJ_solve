import sys
input = sys.stdin.readline
n,m = map(int, input().split())

def printList(li):
  for i in li:
    print(i,end=' ')
  print()

def choose(nums):
  # global n,m
  if len(nums)==m:
    printList(nums)
    return
  for i in range(nums[-1], n+1):
    choose(nums[::] + [i])

for i in range(1,n+1):
  choose([i])