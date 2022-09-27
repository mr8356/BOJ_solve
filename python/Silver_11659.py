import sys
input = sys.stdin.readline
size , quizNum = map(int , input().split())
numbers = list(map(int , input().split()))
temp =0
s = [0]
for i in numbers:
    temp+=i
    s.append(temp)
for x in range(quizNum):
    i,j = map(int , input().split())
    print(s[j]-s[i-1])