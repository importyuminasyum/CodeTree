N, M = map(int, input().split())

dots = [
    tuple(map(int, input().split()))
    for _ in range(M)
]

grid = [
    [0] * N
    for _ in range(N)
]

for i in range(len(dots)):
    x, y = dots[i][0], dots[i][1]
    grid[x - 1][y - 1] = i + 1

for row in range(N):
    print(*grid[row])