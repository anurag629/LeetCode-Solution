# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        n = 0
        temp = head
        while(temp):
            n = n + 1
            temp = temp.next
        
        if(n%2 == 0):
            p = 0
            temp = head
            while(temp):
                p = p + 1
                if(p>n//2):
                    return temp
                temp = temp.next
        else:
            p = 0
            temp = head
            while(temp):
                p = p + 1
                if(p>n//2):
                    return temp
                temp = temp.next
            