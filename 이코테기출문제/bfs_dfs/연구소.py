# p.341 
# https://www.acmicpc.net/problem/14502

from collections import deque
import copy


# 백트래킹
def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    # 세로, 가로
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0

def bfs():
    q = deque()
    graph_c = copy.deepcopy(graph)
    # 바이러스 있는 부분 다 큐에 넣기
    for i in range(n):
        for j in range(m):
            #  바이러스가 있다면
            if graph[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph_c[nx][ny] == 0:
                    graph_c[nx][ny] = 2
                    q.append((nx, ny))
    global result
    safe = 0 
    for a in range(n):
        for b in range(m):
            if graph_c[a][b] == 0:
                safe += 1
    result = max(result, safe)             
                    
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
directions = [(0,1),(0,-1), (1,0),(-1,0)]

result = 0 
make_wall(0)
print(result)