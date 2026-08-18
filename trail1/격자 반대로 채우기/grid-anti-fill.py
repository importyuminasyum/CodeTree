N = int(input())

arr = [
    [0] * N
    for _ in range(N)
]

num_odd = N * N
num_even = 1

if N % 2:
    for col in range(N):
        if col % 2: # 인덱스가 홀수
            for row in range(N - 1, -1, -1):
                arr[row][col] = num_odd
                num_odd -= 1

        else:
            for row in range(N):
                arr[row][col] = num_odd
                num_odd -= 1
else:
    for col in range(N - 1, -1, -1):
        if col % 2: # 인덱스가 홀수
            for row in range(N - 1, -1, -1):
                arr[row][col] = num_even
                num_even += 1

        else:
            for row in range(N):
                arr[row][col] = num_even
                num_even += 1

for row in range(N):
    print(*arr[row])
        