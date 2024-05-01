# https://school.programmers.co.kr/learn/courses/30/lessons/64065
#                    s            ->    result
# "{{2},{2,1},{2,1,3},{2,1,3,4}}" -> [2, 1, 3, 4]
# s는 문자열임

def solution(s):
    num_list = []
    for x in s.split("},"):
        # replace 2번 했을 때: ['2', '2,1', '2,1,3', '2,1,3,4']
        # split 후: [['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]
        # ex) '2,1' -> ","기준으로 split -> ['2', '1']
        num_list.append(x.replace("{", "").replace("}","").split(","))
        
    num_list.sort(key=len)
    answer = []
    for i in num_list:
        for j in i:
            if j not in answer:
                answer.append(j)
            # 숫자로 변환
    return list(map(int,answer))

