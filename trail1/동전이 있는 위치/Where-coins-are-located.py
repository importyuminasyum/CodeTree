N, M = map(int, input().split())

coins = [
    tuple(map(int, input().split()))
    for _ in range(M)
]

grid = [
    [0] * N
    for _ in range(N)
]

for x, y in coins:
    grid[x - 1][y - 1] = 1

for row in range(N):
    print(*grid[row])