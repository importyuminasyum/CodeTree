N = int(input())

pascal = [
    [0] * N
    for _ in range(N)
]

for row in range(N):
    for col in range(N):
        if col == 0 or row == col:
            pascal[row][col] = 1
            continue

        pascal[row][col] = pascal[row - 1][col - 1] + pascal[row - 1][col]

for row in range(N):
    for col in range(N):
        if pascal[row][col]:
            print(pascal[row][col], end = ' ')
    print()