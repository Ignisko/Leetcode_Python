'''

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            new_head = None
            current = head 
            while k > 0:
                next_node = current.next
                current.next = new_head
                new_head = current
                current = next_node
                k -= 1
            return new_head
        
        # Count the number of nodes in the linked list
        node_count = 0 
        current = head
        while current:
            node_count += 1
            current = current.next
        
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy

        while node_count >= k:
            start = prev_group.next
            end = start

            # Move the pointer to the start of the next segment
            for _ in range(k):
                if end: 
                    end = end.next

            # Reverse k nodes
            new_head = reverse(start, k)
            prev_group.next = new_head
            start.next = end

            prev_group = start
            node_count -= k
        
        return dummy.next
