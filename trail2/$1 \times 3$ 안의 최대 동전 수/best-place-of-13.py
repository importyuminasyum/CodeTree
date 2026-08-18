N = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
max_coin = float('-inf')
coin = 0

for row in range(N):
    for col in range(N - 2):
        coin = 0
        for s_col in range(col, col + 3):
            if grid[row][s_col]:
                coin += 1
        max_coin = max(coin, max_coin)

print(max_coin)