# 0 뒤집는 횟수 vs 1 뒤집는 횟수 중 작은 값

S = input()
cnt0 = 0
cnt1 = 0

for i in range(len(S)-1):
    if (S[i] != S[i + 1]):
        if (S[i+1] == "0"):
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))