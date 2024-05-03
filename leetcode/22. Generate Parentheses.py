# https://leetcode.com/problems/generate-parentheses/description/
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(open, close, s):
            # 필요한 길이랑 같다면 (n쌍이 주어짐)
            if len(s) == n * 2:
                answer.append(s)
                return
            if open < n:
                dfs(open + 1, close, s + '(')
            if open > close:
                dfs(open, close + 1, s + ')')
                
        dfs(0, 0, '')
        return answer
