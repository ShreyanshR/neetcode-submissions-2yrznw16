# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        new_head = self.reverseList(head.next)

        if not head.next:
            return head
        
        head.next.next = head
        head.next = None

        return new_head