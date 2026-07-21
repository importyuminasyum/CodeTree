n, m = map(int, input().split())
count = 0

arr = [
    [0 for _ in range(m)]
    for _ in range(n) 
]

for i in range(n):
    for j in range(m):
        count += 1
        arr[i][j] = count
        print(arr[i][j], end=" ")
    print()