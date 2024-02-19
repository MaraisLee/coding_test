# p.323 https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    min_len = len(s)
    # 1부터 중간까지 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        result = ""
        prev = s[0:step]
        now =  s[i:i+step]
        count = 1
        for i in range(step, len(s), step):
            # prev에 저장된 문자열과 같다면 
            if now == prev:
                count += 1
            else:
                if(count >= 2):
                    result +=str(count) + prev
                else:
                    result += prev
                prev = now # 상태초기화
                count = 1
    if(count >= 2):
        result +=str(count) + prev
    else:
        result += prev
        
    min_len = min(min_len, len(result))
    return min_len
