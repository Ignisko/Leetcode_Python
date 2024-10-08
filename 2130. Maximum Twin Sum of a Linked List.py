'''

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, 
if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105

Hint 1
How can "reversing" a part of the linked list help find the answer?
Hint 2
We know that the nodes of the first half are twins of nodes in the second half, 
so try dividing the linked list in half and reverse the second half.
Hint 3
How can two pointers be used to find every twin sum optimally?
Hint 4
Use two different pointers pointing to the first nodes of the two halves of the linked list. 
The second pointer will point to the first node of the reversed half, which is the (n-1-i)th 
node in the original linked list. 
By moving both pointers forward at the same time, we find all twin sums.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode

        maxsum = 0
        e, r = head, prev #ezker, right
        while r:
            maxsum = max(maxsum, e.val + r.val)
            e = e.next
            r = r.next
        
        return maxsum
