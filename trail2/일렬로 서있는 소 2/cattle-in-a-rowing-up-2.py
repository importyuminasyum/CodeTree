# i < j < k 세번 중첩

def dfs():
    count = 0

    for k in range(N):
        for j in range(k):
            for i in range(j):
                if cows[k] >= cows[j] and cows[j] >= cows[i]:
                    count += 1

    return count

N = int(input())
cows = list(map(int, input().split()))
print(dfs())