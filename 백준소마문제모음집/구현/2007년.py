# 수학, 구현, 브론즈1
# https://www.acmicpc.net/problem/1924

a = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())
months =[31,28,31,30,31,30,31,31,30,31,30,31]
day = 0 

# ex) 3월 14일 이면, 2월까지 날짜 + 14 일 이기에 x-1 
for i in range(x-1):
    day += months[i]
    
answer = (day + y) % 7
print(a[answer])
