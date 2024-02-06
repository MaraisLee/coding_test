import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    length = len(food_times)
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1))
        
    t_sum = 0
    prev = 0
    # t_sum + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수
    while t_sum + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        t_sum += (now - prev) * length
        length -= 1
        prev = now
        
    answer = sorted(q, key=lambda x: x[1])
    return answer[(k-t_sum)% length][1]