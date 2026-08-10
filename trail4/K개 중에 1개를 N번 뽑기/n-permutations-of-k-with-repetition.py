def perm(depth):
    if depth == N:
        print(*pick_numbers)
        return

    for i in range(len(numbers)):
        pick_numbers.append(numbers[i])
        perm(depth+1)
        pick_numbers.pop()

K, N = map(int, input().split())
numbers = [i for i in range(1, K+1)]
pick_numbers = []
result = []
perm(0)