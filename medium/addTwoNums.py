'''
For this exercise we are given two non-empty linked lists that represents non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
We are to add the two numbers and return it as a new linked list.


You may assume the two numbers do not contain any leading zero, except the number 0 itself.

eg. 

input 1 = [ 2 -> 4 -> 3 ] => 342 
input 2 = [ 5 -> 6 -> 4 ] => 465
input 1 + input 2 = [ 7 -> 0 -> 8 ] => 807


In this problem, we will traverse both linked lists simultaneously, 
adding corresponding digits along with any carry from the previous addition.

By utlising the carry variable, we can handle cases where the sum of two digits exceeds 9, 
ensuring that we correctly propagate the carry to the next higher digit.

and return the resulting sum as a new linked list in reverse order.

'''




# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # with ListNode access via var.val and var.next print(l1.val)
        l3 = ListNode(0) # dummy head node for new linkedList
        curNode = l3
        # print(l3)  -> ListNode{val: 0, next: None}
        carry = 0 
        while (l1 or l2 or carry):
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            #print(v1,v2)
            s = v1 + v2 + carry 
            #print(s)
            curNode.next = ListNode(s % 10)
            carry = s // 10
            #print(carry)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curNode = curNode.next
        
        return l3.next
    

    