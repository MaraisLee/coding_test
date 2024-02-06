# 모험가 길드

N = int(input())
M_list = list(map(int, input().split()))

group = 0
member = 0

M_list.sort()
for i in M_list:
    member += 1
    if member >= i:
        group +=1
        member = 0

print(group)



