mn , mx = map(int, input().split())
num = [True] * (mx-mn+1)

for i in range(2,int(mx**0.5)+1):
    temp = i*i
    while temp <= mx:
        start_index = int(mn/temp) * temp
        for j in range(start_index , mx+1 , temp):
            if j < mn:
                continue
            if num[j-mn]:
                num[j-mn] = False
        temp*=i
result =0
for i in num:
    if i:
        result+=1
print(result)