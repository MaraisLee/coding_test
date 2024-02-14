# [문제] https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    grid = brown + yellow
    # 가로세로중 한면의 길이는 전체길이의 제곱근을 넘지 않음
    # 즉, n은 항상 작은 쪽 
    for n in range(3, int(grid ** 0.5) + 1):
        if grid % n != 0:
            continue
        m = grid // n
        if (n - 2) * (m - 2) == yellow:
            return [m, n]