arr = [
    [1] * 5
    for _ in range(5)
]

for row in range(5):
    for col in range(5):
        if row > 0 and col > 0:
            arr[row][col] = arr[row][col - 1] + arr[row - 1][col]

for row in range(5):
    print(*arr[row])