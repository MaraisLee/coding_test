# 문자열, 구현, 브론즈2
# https://www.acmicpc.net/problem/8958

n = int(input())

for case in range(n):
    ox = input()
    total = 0
    score = 0
    for i in ox:
        if i == "O":
            score += 1
            total += score
        else:
            score = 0 
    print(total)