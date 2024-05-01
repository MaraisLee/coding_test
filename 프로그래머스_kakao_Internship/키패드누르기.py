# https://school.programmers.co.kr/learn/courses/30/lessons/67256
#       numbers	                     hand	   result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"

def solution(numbers, hand):
    answer = ''
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)
              }
    # 현재 손 위치
    l_hand = '*'
    r_hand = '#'
    for i in numbers:
        # 아래 숫자일 경우, 무조건 'L'
        if i in [1, 4, 7]:
            answer += 'L'
            l_hand = i
        elif i in [3, 6, 9]:
            answer += 'R'
            r_hand = i
        else:
            c_point = keypad[i]
            l_point = keypad[l_hand]
            r_point = keypad[r_hand]
            # 거리 비교 (맨해튼 거리=∣x1−x2∣+∣y1−y2∣)
            l_dist = abs(l_point[0] - c_point[0]) + abs(l_point[1] - c_point[1])
            r_dist = abs(r_point[0] - c_point[0]) + abs(r_point[1] - c_point[1])
            # 작은 거리 쪽 손으로 움직이기
            if l_dist > r_dist:
                answer += 'R'
                r_hand = i
            elif l_dist < r_dist:
                answer += 'L'
                l_hand = i
            else:
                # 거리가 같은 경우
                if hand == 'right':
                    answer += 'R'
                    r_hand = i
                else:
                    answer += 'L'
                    l_hand = i
    return answer
