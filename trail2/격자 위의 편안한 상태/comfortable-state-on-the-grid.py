n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

grid = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

# 어떤 칸을 칠하면서 반복문 돌면서 다 확인
# 세개면 1, 아니면 0

def is_compotable(x, y):
    count = 0
    for dir in range(4):
        nx, ny = x + dirs[dir][0], y + dirs[dir][1]
        if in_range(nx, ny, n) and grid[nx][ny]:
                count += 1
    
    if count == 3:
        return 1
    else:
        return 0

for x, y in points:
    grid[x - 1][y - 1] = 1
    print(is_compotable(x - 1, y - 1))