# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #Edge Cases if list is empty
        if not lists or len(lists) == 0:
            return None

        """
        we will merge basically two sorted list pair by pair, and we have done the pair soln as an easy problem
        """

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None # We are checking this to just see if there is only 1 list, and we do by checking if i+1 list exist

                mergedLists.append(self.mergeList(l1,l2))

            lists = mergedLists

        return lists[0]


    
    def mergeList(self, l1, l2):
        dummy = head = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        #if one of the list finishes early then we will merge the rest of the list
        head.next = l1 or l2

        return dummy.next
        