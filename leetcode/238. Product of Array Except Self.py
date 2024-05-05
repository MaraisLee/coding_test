# https://leetcode.com/problems/product-of-array-except-self/description/
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# 자신을 제외한 곱셉

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        pre = 1
        for i in range(len(nums)):
            answer.append(pre)
            pre *= nums[i]
        pre = 1
        for i in reversed(range(len(nums))):
            answer[i] *= pre
            pre *= nums[i]
        return answer