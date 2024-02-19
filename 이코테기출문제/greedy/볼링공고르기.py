
n, m = map(int,input().split())
k = list(map(int,input().split()))

array = [0] * 11
# i가 같은 무게일 수 0 즉, array[i]에 그 갯수만큼 숫자가 쌓임
for i in k:
    array[i] += 1
    
answer = 0
for i in range(1, m+1):
    # 무게가 i 인, A가 선택할 수 있는 개수 빼기
    n -= array[i]
    # A선택 무게 * B 경우의 수 
    answer += array[i] * n
    
print(answer)