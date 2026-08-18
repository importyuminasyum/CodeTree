N = int(input())

arr = [
    [1] * N
    for _ in range(N)
]

for row in range(N):
    for col in range(N):
        if row and col:
            arr[row][col] = arr[row - 1][col - 1] + arr[row][col - 1] + arr[row - 1][col]

    print(*arr[row])