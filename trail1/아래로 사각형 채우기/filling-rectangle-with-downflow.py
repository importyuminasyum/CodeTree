def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

N = int(input())
num = 0

arr = [
    [0] * N
    for _ in range(N)
]

for col in range(N):
    for row in range(N):
        num += 1
        arr[row][col] = num

for row in range(N):
    print(*arr[row])