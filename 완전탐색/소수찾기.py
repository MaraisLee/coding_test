from itertools import permutations

def solution(numbers):
    answer = []
    # 문자열 numbers를 각각 떼어내기
    nums = [n for n in numbers]
    per = []
    # 각 숫자 조합해서 순열로 만들기 ()
    # len(numbers)가 3개라면 1,2,3개를 순서상관있게 뽑는 각각의 경우의수, 순열을 구한다. 
    for i in range(1, len(numbers) + 1):
            per += list(permutations(nums, i))
    # 각각을 int형으로 변환
    new_nums = [int(("").join(x)) for x in per]
        
    for i in new_nums:
        if i < 2:
            continue
        check = True 
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            # answer += i : Error ; 'int' object is not iterable
            answer.append(i)
            
    return len(set(answer))