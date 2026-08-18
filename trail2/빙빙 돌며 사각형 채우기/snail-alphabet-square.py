N, M = map(int, input().split())

# Please write your code here.
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

direction = 0

snail = [
    [0] * M
    for _ in range(N)
]

x, y = 0, 0
snail[x][y] = 'A'

for num in range(2, N * M + 1):
    nx, ny = x + dirs[direction][0], y + dirs[direction][1]

    if not in_range(nx, ny, N, M) or snail[nx][ny]:
        direction = (direction + 1) % 4
        nx, ny = x + dirs[direction][0], y + dirs[direction][1]

    x, y = nx, ny
    snail[x][y] = chr((num - 1) % 26 + 65)

for row in range(N):
    print(*snail[row])
