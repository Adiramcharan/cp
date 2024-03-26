# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        l=len(stack)
        k=k%l
        if k!=l:
            stack=stack[-k:]+stack[:l-k]
        i=0
        head=ListNode()
        tmp=head
        while i<l:
            head.next=stack[i]
            head=head.next
            i+=1
        head.next=None
        return tmp.next
