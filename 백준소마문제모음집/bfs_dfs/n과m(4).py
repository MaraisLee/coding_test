# 백트레킹 dfs, 실버3
# https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())
array = []

def dfs(start):
    if len(array) == m:
        print(' '.join(map(str, array)))
        return
    
    for i in range(start, n + 1):
        array.append(i)
        dfs(i)
        array.pop()

dfs(1)

