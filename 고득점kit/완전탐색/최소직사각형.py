# [링크] https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    for i in sizes:
        i.sort()
    width = [a for a, b in sizes]
    height = [b for a, b in sizes]
    return max(width) * max(height)