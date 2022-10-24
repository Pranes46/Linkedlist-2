# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        lenA = 0 # assigning 0 
        lenB = 0 # assigning 0
        pa = headA # assigning pointer to head A
        pb = headB # assigning pointer to head B
        
        while pa!=None: # the loop will run until the pa reaches null
            lenA+=1 #incrementing the pointer lenA
            pa = pa.next  #incrementing the PA pointer
            
        while pb!=None: # the loop will run until the pa reaches null
            lenB+=1 #incrementing the pointer lenB
            pb = pb.next #incrementing the PB pointer
            
        pa = headA #assigning pointer to head A
        pb = headB # assigning pointer to head B
        
        while lenA>lenB: #loop will break when the len a is less than len b
            pa = pa.next  #incrementing the pointer
            lenA-=1 #decrementing the length
            
        while lenA<lenB: #loop will break when the len B is less than len A
            pb = pb.next #incrementing the pointer
            lenB-=1  #decrementing the length
            
        while pa!=pb: # run until pa not equl to pb
            pa = pa.next # incrementing 1 node
            pb = pb.next # incrementing 1 node
            
        return pa
        
        
        