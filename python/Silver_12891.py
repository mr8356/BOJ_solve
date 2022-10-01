#slide Window
import sys
input = sys.stdin.readline
length , passLength = map(int , input().split())
dna = input()
#ACGT
Goal = list(map(int , input().split()))
contain = [0,0,0,0]
start_index , end_index = 0 , passLength-1
cnt = 0


def add(ch):
    if ch == 'A':
        contain[0]+=1
    elif ch=='C':
        contain[1]+=1
    elif ch=='G':
        contain[2]+=1
    elif ch=='T':
        contain[3]+=1

def remove(ch):
    if ch == 'A':
        contain[0]-=1
    elif ch=='C':
        contain[1]-=1
    elif ch=='G':
        contain[2]-=1
    elif ch=='T':
        contain[3]-=1

for i in range(passLength):
    add(dna[i])
if contain[0]>=Goal[0]:
        if contain[1]>=Goal[1]:
            if contain[2]>=Goal[2]:
                if contain[3]>=Goal[3]:
                    cnt+=1

while end_index<length-1:
    remove(dna[start_index])
    start_index+=1
    end_index+=1
    add(dna[end_index])
    if contain[0]>=Goal[0]:
        if contain[1]>=Goal[1]:
            if contain[2]>=Goal[2]:
                if contain[3]>=Goal[3]:
                    cnt+=1
    
print(cnt)