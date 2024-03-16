# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        dec=0
        lenght=0
        while stack:
            dec=dec+math.pow(2,lenght)*stack.pop()
            lenght+=1
        return int(dec)
