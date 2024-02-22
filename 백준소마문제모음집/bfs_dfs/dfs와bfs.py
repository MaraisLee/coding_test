# dfs bfs, 실버2
# https://www.acmicpc.net/problem/1260

# 시간복잡도가 낮은 depue 사용
from collections import deque

n, m, v = map(int, input().split())
# 그래프 초기화 / 0번 인덱스 안 사용할 거라서 n+1개 생성. 
# 즉, 총 0번부터 n번까지의 리스트 생성
graph = [[False] * (n + 1) for _ in range(n + 1)] # ex) n = 2, [[False, False, False], [False, False, False], [False, False, False]]

# 연결된 정점을 입력
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# dfs, bfs 각각의 방문여부 담을 리스트
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(v):
    visited1[v] = True
    # 방문 후, 해당 정점 출력(옆으로 나열됨) 
    print(v, end = " ")
    for i in range(1, n + 1):
        # 방문기록이 없고, 값이 연결되있다면 
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    # 방문할 곳을 순서대로 넣을 큐
    q = deque([v])
    visited2[v] = True
    while q:
        # 큐 맨 앞의 값을 꺼내서 출력 
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            # 방문기록이 없고, 값이 연결되있다면 
            if not visited2[i] and graph[v][i] == 1:
                # i를 큐에 추가하면서 방문한 곳으로 기록한다. 
                q.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)