N = int(input())

odd_count = 1
even_count = N

for i in range(N * 2):    
    if i % 2:
        print('* ' * odd_count)
        odd_count += 1
    else:
        print('* ' * even_count)
        even_count -= 1

