# p.322
# 문자인지 알파벳이지 구별후 오름차순 정렬

s = input()
result = []
num = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        num += int(i)

result.sort()
if num != 0:
    # 문자로 변환해서 리스트에 넣기 
    result.append(str(num))
# 리스트를 문자열로 변환해서 출력
print("".join(result)) 