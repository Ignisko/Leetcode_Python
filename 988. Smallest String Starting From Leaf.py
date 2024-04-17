'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

 

Example 1:


Input: root = [0,1,2,3,4,3,4]
Output: "dba"
Example 2:


Input: root = [25,1,3,1,3,0,2]
Output: "adz"
Example 3:


Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
 

Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # Initialize the smallest string with a placeholder higher than any possible valid string
        self.smallest = "~"  # '~' has a higher ASCII value than any lowercase letter

        def dfs(node, path):
            if node:
                # Build the string as we move back up the tree
                path = chr(node.val + ord('a')) + path

                # If it's a leaf node, compare the path to the smallest
                if not node.left and not node.right:
                    self.smallest = min(self.smallest, path)

                # Recurse down to both children
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return self.smallest
