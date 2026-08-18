def dfs(parentheses):
    count = 0
    for i in range(len(parentheses)):
        if parentheses[i] == '(':
            count += parentheses.count(')', i)
    return count

parentheses = input()

print(dfs(parentheses))