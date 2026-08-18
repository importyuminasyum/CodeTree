dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 하 우 상 좌

def in_range(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

N, M = map(int, input().split())
direction = 0

snail = [
    [0] * M
    for _ in range(N)
]

x, y = 0, 0
snail[x][y] = 1

for num in range(2, N * M + 1):
    nx, ny = x + dirs[direction][0], y + dirs[direction][1]

    if not in_range(nx, ny, N, M) or snail[nx][ny]:
        direction = (direction + 1) % 4
        nx, ny = x + dirs[direction][0], y + dirs[direction][1]

    x, y = nx, ny
    snail[x][y] = num

for row in range(N):
    print(*snail[row])
