# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp=head
        while temp:
            c+=1
            temp=temp.next
        temp=head
        for i in range(c//2):
            temp=temp.next
        return temp