# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head 
        regular = head 
        slow = ListNode(0)
        slow.next = head 
        result = slow
        count = 1
        while head :
            count +=1 
            head = head.next 
            
        n = count -n - 1
        while n > 0:
            n -=1 
            regular = regular.next 
            slow = slow.next 
            
        slow.next = regular.next 
        return (result.next)