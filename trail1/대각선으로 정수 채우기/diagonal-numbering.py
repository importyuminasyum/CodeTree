N, M = map(int, input().split())
num = 0

arr = [
    [0] * M 
    for _ in range(N)
]

for check in range(N * M):
    for row in range(N):
        for col in range(M):
            if row + col == check:
                num += 1
                arr[row][col] = num

for row in range(N):
    print(*arr[row])