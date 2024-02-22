# 이진탐색, 실버4
# https://www.acmicpc.net/problem/1920

import bisect

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

def binary(list, target):
    idx = bisect.bisect_left(list, target)
    
    if idx < len(list) and list[idx] == target:
        return 1
    else: 
        return 0
for i in m_list:
    print(binary(n_list, i)) 