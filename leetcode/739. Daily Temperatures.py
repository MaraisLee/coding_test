# https://leetcode.com/problems/daily-temperatures/description/
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):  # 온도 리스트를 순회하면서 온도와 인덱스를 가져옴
            # 스택이 비어있지 않고, 스택의 맨 위 온도가 현재 온도보다 작을 때
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()  # 스택에서 가장 최근의 인덱스를 꺼냄
                # 정답 리스트에 현재 인덱스와 이전 인덱스의 차이를 저장
                answer[prev_index] = i - prev_index
            stack.append(i)  # 현재 인덱스를 스택에 추가

        return answer  # 정답 반환s
