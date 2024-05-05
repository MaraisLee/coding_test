# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                answer.append(level)

        return answer


# 2번째 방법
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        temp = [root]
        level = 0

        while len(temp) > 0:
            res.append([])
            for i in range(len(temp)):
                t = temp.pop(0)
                res[level].append(t.val)
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)

            level += 1

        return res
