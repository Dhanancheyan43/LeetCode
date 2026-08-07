# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next
        if c==1:
            return None
        m=c//2
        temp=head
        for i in range(m-1):
            temp=temp.next
        temp.next=temp.next.next
        return head