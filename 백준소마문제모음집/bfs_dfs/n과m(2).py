# 백트래킹 dfs, 실버3
# https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())
array = []

# 시작숫자를 넣음으로써 자동으로 오름차순정렬로 array에 쌓임
def dfs(start):
    if len(array) == m:
        print(' '.join(map(str, array)))
        return
    
    for i in range(start, n + 1):
        if i not in array:
            array.append(i)
            dfs(i + 1)
            array.pop()
            
dfs(1)