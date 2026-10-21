n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def cal_coin(sr, sc, er, ec):
    count = 0
    for r in range(sr, er):
        for c in range(sc, ec):
            if grid[r][c]:
                count += 1
    return count

result = 0
for r in range(n - 2):
    for c in range(n - 2):
        result = max(result, cal_coin(r, c, r + 3, c + 3))
print(result)