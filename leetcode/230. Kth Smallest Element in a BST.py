# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

class Solution:
    def kthSmallest(self, root, k):
        answer = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                answer.append(root.val)
                inOrder(root.right)
                
        inOrder(root)
        # k는 1부터 시작
        return answer[k-1]