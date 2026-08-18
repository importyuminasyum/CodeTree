# 1번 집, 2번 집 각각 Ai 값 곱하기 인덱스 - 해당 집의 합
def dfs():
    global min_move_length

    for i in range(N):
        length = 0

        for j in range(N):
            length += A[j] * abs(j - i)
    
        min_move_length = min(length, min_move_length)

min_move_length = float('inf')
N = int(input())
A = list(map(int, input().split()))
dfs()
print(min_move_length)