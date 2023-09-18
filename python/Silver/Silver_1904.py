n = int(input())
D = [0] * (n+2)
D[1] = 1 # 1
D[2] = 2 # 11 00
for i in range(3,n+1):
    D[i] = (D[i-1] + D[i-2]) % 15746
print(D[n])