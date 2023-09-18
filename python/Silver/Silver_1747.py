#에라토스테네스의 체
n = int(input())
num = [0]*(1000001)
for i in range(2,1000001):
    num[i] = i

def isPelindrome(t):
    n_string = str(t)
    length = len(n_string)
    for i in range(int(length/2)+1):
        if n_string[i] != n_string[length-1-i]:
            return False
    return True

for i in range(2,1000001):
    if num[i] == 0:
        continue
    for j in range(i+i ,1000001,i):
        num[j] = 0

result = 0
for i in range(n, 1000001):
    if num[i]!=0 and isPelindrome(i):
        result = i
        break
if result == 0:
    result = 1003001
print(result)

#원래 (테스트 코드)
# n = int(input())
# num = [0]*(10000001)
# for i in range(2,10000001):
#     num[i] = i

# def isPelindrome(t):
#     n_string = str(t)
#     length = len(n_string)
#     for i in range(int(length/2)+1):
#         if n_string[i] != n_string[length-1-i]:
#             return False
#     return True

# for i in range(2,10000001):
#     if num[i] == 0:
#         continue
#     for j in range(i+i ,10000001,i):
#         num[j] = 0

# for i in range(n, 10000001):
#     if num[i]!=0 and isPelindrome(i):
#         print(i)
#         break
            