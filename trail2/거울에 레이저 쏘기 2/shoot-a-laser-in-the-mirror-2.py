n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 하 좌 상 우

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def find_xy(k):
    direction = (k - 1) // n
    idx = (k - 1) % n
    if direction == 0:
        x, y = 0, idx
    elif direction == 1:
        x, y = idx, n - 1
    elif direction == 2:
        x, y = n - 1, n - 1 - idx
    else:
        x, y = n - 1 - idx, 0
    return x, y, direction
    
def transfer(slash, direction):
    if slash == '/':
        return [1, 0, 3, 2][direction]
    else:
        return [3, 2, 1, 0][direction]

count = 0
x, y, direction = find_xy(k) # 초기 시작 값

while in_range(x, y, n):
    count += 1
    direction = transfer(grid[x][y], direction)

    x, y = x + dirs[direction][0], y + dirs[direction][1]

print(count)