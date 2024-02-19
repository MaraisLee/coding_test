# 곱하기 혹은 더하기
# - 0, 1인경우 에는 +가 나음

S = input()

# 첫째숫자 넣어놓기 
answer = int(S[0])

for i in range(1, len(S)):
    if int(S[i]) <= 1 or answer<=1:
        answer += int(S[i])
    else:
        answer *= int(S[i])
            
print(answer)