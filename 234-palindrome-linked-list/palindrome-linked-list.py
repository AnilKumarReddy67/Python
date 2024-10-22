# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front=head
        def trav(cur):
            if cur is None:
                return True
            if trav(cur.next)==False:
                return False
            if self.front.val!=cur.val:
                return False
            self.front=self.front.next
            return True
            
        return trav(head)
