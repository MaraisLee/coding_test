# p.346

# 균형잡힌 괄호 문자열
def balanced(p):
    # 왼쪽 괄호 개수
    count = 0 
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        # '('와 ')'의 개수가 같다면, 균형잡힌 괄호 문자열
        if count == 0:
            return i

# 올바를 괄호 문자열
def correct(p):
    # 왼쪽 괄호 개수
    count = 0 
    for i in p:
        if  i == '(':
            count += 1
        else:
            # '(' 없이 내려온 경우
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    # u는 균형잡힌 문자열인 상태
    index  = balanced(p)
    # 문자열 나누기
    u = p[:index + 1]
    v = p[index + 1:]
    if correct(u):
        # 3단계
        answer = u + solution(v)
    # 4단게 실행 
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        # 괄호 방향 뒤집기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer