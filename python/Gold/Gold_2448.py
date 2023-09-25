N = int(input())

# 길이가 3인 초기 그래프
graph = [[" ", " ", "*", " ", " "], [" ", "*"," ", "*", " "], ["*", "*", "*", "*", "*"]]

# 길이가 3인 초기 그래프를 받아서 3*2 = 6을 호출한다
# 6에서는 길이가 3인 그래프를 좌우로 복제시켜서 6인그래프를 만들고
# 길이가 6인그래프를 넘겨줘서 다음 길이가 6*2=12인 그래프를 6인그래프 두개를 복제해서 만들도록 한다
def makeTri(n, before):
    if n == N:
        return before
    # 이전 그래프의 가로 길이
    length = 2*n-1
    # 새 그래프의 가로길이
    newLength = 2*2*n-1
    after = [[" "]*(newLength) for _ in range(2*n)]
    # 기존 그래프 1차적으로 복사할때 시작할 인덱스
    startIdx = (newLength-length)//2
    # 기존 그래프 1차적으로 복사
    for i in range(n):
        after[i][startIdx:startIdx+length] = before[i]

    # 기존 그래프를 양옆에 하나씩 복사
    for i in range(n):
        after[n+i] = before[i] + [" "] + before[i]
    return makeTri(n*2, after)

# 3부터 시작해서 N될때까지 재귀
graph = makeTri(3, graph)

#그래프 출력
for i in range(N):
    print(''.join(graph[i]))
