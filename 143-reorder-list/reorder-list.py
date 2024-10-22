# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # using slow and fast pointers to divide the list into half
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next #2nd half
        prev=slow.next=None #first half end to None
        while second: # reversing 2nd half
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        first,second=head,prev
        while second: #2nd half will have less than or equal number of nodes than 1st half
            t1,t2=first.next,second.next
            first.next=second
            second.next=t1
            first,second=t1,t2
        

        