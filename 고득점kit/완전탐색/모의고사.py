# [링크] https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []
    
    for idx, v in enumerate(answers):
        if v == first[idx % len(first)]:
            score[0] += 1
        if v == second[idx % len(second)]:
            score[1] += 1
        if v == third[idx % len(third)]:
            score[2] += 1
    
    for idx, v in enumerate(score):
        if v == max(score):
            answer.append(idx+1)
    return answer