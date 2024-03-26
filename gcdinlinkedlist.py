# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp2 = head
        while head.next:
            n1 = head.val
            n2 = head.next.val
            #n3 = self.gcd(n1,n2)
            n3 = math.gcd(n1,n2)
            tmp = ListNode()
            tmp.val = n3
            tmp.next = head.next
            head.next = tmp
            head = head.next.next
            #if not head:
            #break
        return tmp2
