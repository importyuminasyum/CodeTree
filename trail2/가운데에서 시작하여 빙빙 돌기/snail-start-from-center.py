n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 좌 상 우 하

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

direction = 0

x, y = n - 1, n - 1
grid[x][y] = n * n

for num in range(n * n - 1, 0, -1):
    nx, ny = x + dirs[direction][0], y + dirs[direction][1]

    if not in_range(nx, ny, n) or grid[nx][ny]:
        direction = (direction + 1) % 4
        nx, ny = x + dirs[direction][0], y + dirs[direction][1]

    x, y = nx, ny
    grid[x][y] = num

for row in range(n):
    print(*grid[row])
