'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        qu = deque([(root, 1)])
        maxsum = float('-inf')
        maxlvl = 1

        while qu:
            curlvl = qu[0][1]
            cursum = 0

            while qu and qu[0][1] == curlvl:
                node, lvl = qu.popleft()
                cursum += node.val

                if node.left:
                    qu.append((node.left, lvl + 1))
                if node.right:
                    qu.append((node.right, lvl + 1))

            if cursum > maxsum:
                maxsum = cursum
                maxlvl = curlvl
        
        return maxlvl

                
