# https://leetcode.com/problems/rotate-image/description/
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 깊은 복사 (메모리 주소도 다름)
        old_matrix = [arr[:] for arr in matrix]
        length = len(matrix)
        for i in range(length):
            # 0, 1, 2
            for j in range(length):
                # case1을 수기로 적어봤을 때, 아래의 점화식 도출
                matrix[j][length-i-1] = old_matrix[i][j]
