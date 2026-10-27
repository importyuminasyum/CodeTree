def turn_over(start, end, dir):
    if dir == 'R':
        for i in range(start, start + end):
            tiles[i] = 'R'
        return start + end - 1

    else:
        for i in range(start, start - end, -1):
            tiles[i] = 'L'
        return start - end + 1

n = int(input())
tiles = [''] * 200001

pointer = 10000
for _ in range(n):
    x, dir = input().split()
    x = int(x)
    pointer = turn_over(pointer, x, dir)

print(tiles.count('L'), tiles.count('R'))