# https://school.programmers.co.kr/learn/courses/30/lessons/64064?language=python3
#                       user_id	                           banned_id	  result
# ["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"]	    2

from itertools import permutations


def check_id(users, banned_id):
    # 같이 for문을 돌리면서
    for u, b in zip(users, banned_id):
        # 길이가 다르면 다른 아이디
        if len(u) != len(b):
            return False
        # user_id를 돌리면서
        for i in range(len(u)):
            # 같은 인덱스의 알파벳이 다른데 가려진 경우도 아닐 때
            if u[i] != b[i] and b[i] != '*':
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    # 나올 수 있는 조합 우선 다 찾기 p(array, 숫자)
    candidates_list = list(permutations(user_id, len(banned_id)))

    for candidates in candidates_list:
        if check_id(candidates, banned_id):
            # 이미 answer에 들어가 있는지 비교하기위해 정렬
            candidates = sorted(candidates)
            if candidates not in answer:
                answer.append(candidates)

    return len(answer)
