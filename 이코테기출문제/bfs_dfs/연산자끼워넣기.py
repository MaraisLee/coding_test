# p.349
# https://www.acmicpc.net/problem/14888

n = int(input())
num= list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 1dj
maxi = -1e9
mini = -1e9

def dfs(depth, total,add, sub, mul, div ):
    global maxi, mini
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    if add:
        dfs(depth + 1, total + num[depth], add -1,sub, mul, div )
    if sub:
        dfs(depth + 1, total - num[depth], add ,sub -1, mul, div )
    if mul:
        dfs(depth + 1, total * num[depth], add ,sub, mul -1, div )
    if div:
        dfs(depth + 1, int(total / num[depth]), add ,sub, mul, div-1 )
        

dfs(1, num[0], add, sub, mul, div)
print(maxi)
print(mini)