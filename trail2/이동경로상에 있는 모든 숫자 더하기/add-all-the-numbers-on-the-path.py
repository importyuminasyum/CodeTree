dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상 우 하 좌

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

N, T = map(int, input().split())
score = 0
commands = input()
direction = 0
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

x, y = N // 2, N // 2
score += grid[x][y]
# 초기값 설정
# F가 나오면 다음 갈 수 있는지 확인하고 되면 가기, 안되면 가지 않기
for command in commands:
    if command == 'F':
        if in_range(x + dirs[direction][0], y + dirs[direction][1], N):
            x, y = x + dirs[direction][0], y + dirs[direction][1]
            score += grid[x][y]

    elif command == 'L':
        direction = (direction - 1) % 4

    else:
        direction = (direction + 1) % 4

print(score)
    