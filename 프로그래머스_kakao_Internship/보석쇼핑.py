# https://school.programmers.co.kr/learn/courses/30/lessons/67258/solution_groups?language=python3
#                                       gems	                        result
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
# 1. 포인터 나눠서 생각

def solution(gems):
    N = len(gems)
    answer = [0, N - 1]
    # 중복되지 않은 보석의 종류
    kind = len(set(gems))
    # 2 points 설정
    left, right = 0, 0
    # 우선 첫번째 보석만 1개로 넣어줌
    dic = {gems[0]: 1}
    # 두 포인트가 전체 길이를 넘지 않는 동안
    while left < N and right < N:
        # 지금까지 발견한 보석이 전체 보석 종류보다 적은 경우
        if len(dic) < kind:
            # 오른쪽 포인트를 한칸 더 늘리기
            right += 1
            # 그 때 마지막에 닿는다면 빠져나오기
            if right == N:
                break
            # 딕셔너리 안에 찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값') 사용
            dic[gems[right]] = dic.get(gems[right], 0) + 1
        else:
            # 투 포인트의 길이가 answer에 담긴 길이보다 작은 경우, 그걸로 대체 (최소 길이 찾는중이므로)
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            # 해당 타입이 한 개있을 경우 아예 없애기
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            # 왼쪽 포인트 이동
            left += 1

    return [answer[0]+1, answer[1]+1]
