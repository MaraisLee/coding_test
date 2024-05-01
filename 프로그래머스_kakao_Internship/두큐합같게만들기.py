# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# [3, 2, 7, 2]	[4, 6, 5, 1] -> 2

from collections import deque


def solution(queue1, queue2):
    # 큐에 넣고
    q1, q2 = deque(queue1), deque(queue2)
    # 각각 합을 구한다
    q1_sum, q2_sum = sum(q1), sum(q2)
    # 길이 제한이 있기 때문에 범위를 걸고
    for i in range(300000):
        # 만약 각각의 합이 같다면 그 시도횟수만큼 리턴
        if q1_sum == q2_sum:
            return i
        # 한 쪽이 큰 경우에는 큰 부분의 원소를 빼서 작은 부분에 넣어 주기, sum은 최초 한번만 선언되기때문에 반드시 업데이트 해주기
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        else:  # q2_sum이 q1_sum보다 클 때
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
    # 값이 같아지지 않으면 -1을 반환
    return -1
