# bfs, 실버1
# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())
# 움직일 수 있는 최대 값
max_num = 100000
visited = [0] * (max_num + 1) 

def bfs():
    # 수빈이의 출발점 위치 큐에 삽입
    q = deque([n])
    while q: 
        x = q.popleft()
        # 수빈이랑 동생위치가 같다면 반복문 종료 
        if x == k:
            print(visited[x])
            break
        # 이동할 수 있는 방향에 대해
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max_num and not visited[i]:
                # 원래 있던 것에 시간 1초 더해줌
                visited[i] = visited[x] + 1
                # 큐에 추가
                q.append(i)
    
bfs()