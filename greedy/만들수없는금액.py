# 정렬 후, 작은 값부터 돌리면서 조합시 안되는 최솟값찾기

N = int(input())
d_list = list(map(int, input().split()))

d_list.sort()

# 목표값 설정
target = 1

for coin in d_list:
    # 현재 동전이 목표값보다 크면, 해당 목표값은 만들 수x
    if (coin > target):
        break
    target += coin
    
print(target)
