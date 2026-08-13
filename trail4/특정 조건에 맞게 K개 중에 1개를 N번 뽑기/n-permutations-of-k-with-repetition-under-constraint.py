K, N = map(int, input().split())
pick_numbers = []

# Please write your code here.
def dfs(depth):
    if depth == N:
        print(*pick_numbers)
        return

    for i in range(1, K + 1):
        if depth >= 2 and i == pick_numbers[-1] and i == pick_numbers[-2]:
            continue
        pick_numbers.append(i)
        dfs(depth + 1)
        pick_numbers.pop()
dfs(0)