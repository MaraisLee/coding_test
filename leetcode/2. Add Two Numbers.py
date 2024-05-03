# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def node2list(self, node1: ListNode) -> List:
        list1 = []
        while node1 != None:
            list1.append(node1.val)
            node1 = node1.next
        return list1

    def list2node(self, list1: ListNode) -> ListNode:
        result_node = ListNode()
        for i, num in enumerate(list1):
            if i == 0:
                result_node.val = num
            else:
                node = result_node
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)
        return result_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = self.node2list(l1)
        list2 = self.node2list(l2)

        list1.reverse()
        list2.reverse()
        # list -> 문자열 -> 숫자
        num1 = int(''.join([str(x) for x in list1]))
        num2 = int(''.join([str(x) for x in list2]))

        # 합해서 다시 list -> reverse
        answer = list(str(num1 + num2))
        answer.reverse()
        return self.list2node(answer)
