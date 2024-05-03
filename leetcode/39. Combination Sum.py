# https://leetcode.com/problems/combination-sum/description/
# 합쳐서 target 수가 되는 조합, 한 사람 여러번 쓰일수 0

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        output = []

        def combination(idx, count):
            if count >= target:
                if count == target:
                    answer.append(output[:])
                return
            # 숫자가 target보다 커진경우에는 빠져나와서 pop으로 마지막 숫자빼고 다음 꺼 넣어서 다시
            if idx >= len(candidates):
                return

            output.append(candidates[idx])
            combination(idx, count + candidates[idx])
            output.pop()
            combination(idx+1, count)

        combination(0, 0)
        return answer
