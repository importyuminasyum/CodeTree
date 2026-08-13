n = int(input())

# Please write your code here.
visited = [0] * (n + 1)
pick_numbers = []

def dfs(depth):
    if depth == n:
        print(*pick_numbers)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        pick_numbers.append(i)
        visited[i] = 1
        dfs(depth + 1)
        pick_numbers.pop()
        visited[i] = 0

dfs(0)

