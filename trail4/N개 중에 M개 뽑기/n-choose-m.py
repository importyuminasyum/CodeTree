def comb(depth, idx):
    if depth == M:
        print(*pick_numbers)
        return

    for i in range(idx, N + 1):
        pick_numbers.append(i)
        comb(depth + 1, i + 1)
        pick_numbers.pop()

pick_numbers = []
N, M = map(int, input().split())
comb(0, 1)