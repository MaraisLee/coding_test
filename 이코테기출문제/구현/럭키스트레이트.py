# p.321
# 반을 쪼개서 먼저 더해주고 나머지 반틈은 뺐을 때 0이면 동일한 합이라는 의미.

n = input()
length = len(n)
sum = 0 

for i in range(length // 2):
    sum += int(n[i])
for i in range(length // 2, length):
    sum -= int(n[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")