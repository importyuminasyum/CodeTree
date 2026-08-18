N, M = map(int, input().split())
num = 0

arr = [
    [0] * M
    for _ in range(N)
]

for col in range(M):
    if col % 2:
        for row in range(N - 1, -1, -1):
            arr[row][col] = num
            num += 1

    else:
        for row in range(N):
            arr[row][col] = num
            num += 1

for row in range(N):
    print(*arr[row])