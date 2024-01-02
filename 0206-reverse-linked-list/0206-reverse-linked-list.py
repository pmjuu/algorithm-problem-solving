# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = []
        node = head
        
        while node:
            stack.append(node.val)
            node = node.next

        reversed_list = ListNode(stack.pop())
        
        def add_node(node, stack):
            if not stack:
                return
            
            node.next = ListNode(stack.pop())
            add_node(node.next, stack)
        
        add_node(reversed_list, stack)
            
        return reversed_list