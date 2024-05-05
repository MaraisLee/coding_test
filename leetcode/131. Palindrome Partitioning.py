# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        part = []
        # ex) 기러기, 토마토
        def isPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right - 1
            return True

        def dfs(i):
            if i == len(s):
                answer.append(part[:])
                return

            for j in range(i, len(s)):
                if isPali(i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return answer
