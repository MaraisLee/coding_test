# 백트레킹 dfs, 실버3
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())
array = []

def dfs():
    # array 배열에 m개의 숫자만큼 차있으면 print
    if len(array) == m:
        # 리스트 array의 각 요소를 문자열로 변환 -> 이를 빈 칸을 사이에 두고 하나의 문자열로 합치기 -> map() 함수를 사용하여 각 요소를 문자열로 변환 -> join()으로 이들을 하나의 문자열로 결합
        print(' '.join(map(str, array)))
        return
    
    for i in range(1, n+1):
        # i가 없다면 (중복 제외)
        if i not in array:
            array.append(i)
            dfs()
            array.pop()
            #  백트레킹 특징
            #  현재 s=[1]인 상태에서 다음숫자를 넣기위하여 가지치기하기(재귀함수)
            #   -> 만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.
            #       s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
            #            출력   pop(2)   출력    pop(3)    출력

dfs()


