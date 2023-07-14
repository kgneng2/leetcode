# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/add-two-numbers/description/
class Solution:
    def toReverse(self, i1: Optional[ListNode]):
        a1=[]
        nextNode= i1
    
        while True:
            a1.append(str(nextNode.val))
            if nextNode.next is None:
                break
            else:
                nextNode = nextNode.next
        
        print(a1)
        a1.reverse()
        print(a1)
        

        return int(''.join(a1))


    def createListNodeList(self, val):
        if not val:
            return None

        head = ListNode(val[0])
        head.next = self.createListNodeList(val[1:])
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.toReverse(l1)
        r2 =  self.toReverse(l2)
        res = r1 + r2 

        r_list = list(str(res))
        r_list.reverse()
        print(r_list)
        res = self.createListNodeList(r_list)

        return res 
