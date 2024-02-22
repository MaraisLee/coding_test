# 이진탐색, 실버5
# https://www.acmicpc.net/problem/10815

# 조건의 최댓값이 500,000 ^2 ->  큰 수를 돌게 될 때,
# A1. dictionary 사용 (선형탐색)
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# dictionary가 list 보다 시간 덜 걸림
dic = {}
for i in m_list:
    dic[i] = 0 

for x in n_list:
    if x in dic:
        dic[x] = 1

for d in dic:
    print(dic[d], end= ' ')

-----------------

# A2. 이진탐색

import bisect

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 이진탐색에 정렬 필수!
n_list.sort()

def binary(list, target): 
    # 자기자신앞애 인덱스가 하나 더 생긴다고 생각. 결국 원래 자기자신 인덱스
    idx = bisect.bisect_left(list, target)
    # 항상 인덱스는 배열의 전체 길이보다 1개 더 크다 (0부터 시작하니깐)
    if idx < len(list) and list[idx] == target:
        return 1
    else:
        return 0

for i in m_list:
    print(binary(n_list, i), end= " ")
    


    