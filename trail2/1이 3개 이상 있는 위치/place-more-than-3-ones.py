def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
grid = [input().split() for _ in range(n)]
result = 0

for r in range(n):
    for c in range(n):
        count = 0

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not in_range(nr, nc):
                continue

            if grid[nr][nc] == '1':
                count += 1
        
        if count >= 3:
            result += 1

print(result)