n, s = map(int, input().split())
nums = list(map(int, input().split()))
subtotal = [0]*(n+1)
subtotal
for i in range(n):
  subtotal[i+1] = subtotal[i] + nums[i]

start = 1
end = 1
length = 10**6
while start<=end:
  total = subtotal[end] - subtotal[start-1]
  if end == n:
    if total >= s:
      length = min(length, end - start + 1)
      start += 1
    if total < s:
      break
  else:
    if total < s:
      end += 1
    if total >= s:
      length = min(length, end - start + 1)
      start += 1

if length == 10**6:
  print(0)
else:
  print(length)

