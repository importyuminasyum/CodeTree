N = int(input())

for i in range(1, N * 2):
    j = abs(N - i)
    print(' ' * j + '* ' * (N - j))
