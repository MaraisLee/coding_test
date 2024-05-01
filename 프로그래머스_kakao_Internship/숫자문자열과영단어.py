# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
#       s          -> result
# "one4seveneight" -> 1478

def solution(s):
    # dictinary 생성
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
    answer = s
    # key와 value를 한꺼번에 for문을 반복하려면 items() 
    for key, value in dic.items():
        # replace(old, new, [count]) -> replace("찾을값", "바꿀값", [바꿀횟수]) 왼쪽부터 시작
        answer = answer.replace(key, value)
    return int(answer)
