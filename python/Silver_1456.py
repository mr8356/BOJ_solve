#에라토스테네스의 체
a,b = map(int , input().split())
num = [0]*(int(b**0.5)+1)
cnt = 0
for i in range(2,int(b**0.5)+1):
    num[i] = i
for i in range(2,int(b**0.5)+1):
    if num[i] == 0:
        continue
    else:
        for j in range(i+i ,int(b**0.5)+1,i):
            num[j] = 0
        temp = i**2
        while True:
            if temp <= b:
                if temp >= a:
                    cnt+=1
            else:
                break
            temp*=i
print(cnt)