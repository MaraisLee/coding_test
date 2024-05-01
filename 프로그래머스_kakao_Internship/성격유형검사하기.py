# https://school.programmers.co.kr/learn/courses/30/lessons/118666
#               survey	                choices	    result
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# 같은 점수인 경우, 알파벳순 정렬

def solution(survey, choices):
    answer = ''
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for s, c in zip(survey, choices):
        if c > 4:
            dic[s[1]] += c-4
        elif c < 4:
            dic[s[0]] += 4-c
    li = list(dic.items())
    # 2개씩 한 유형
    for i in range(0, 8, 2):
        if li[i][1] < li[i+1][1]:
            # 알파벳부분 정답에 넣기
            answer += li[i+1][0]
        # 같은 경우에는 알파벳순 정렬, 즉. 앞에 나온 것
        else:
            answer += li[i][0]

    return answer
