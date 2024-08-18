'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000


🌟 437. Path Sum III | DFS + Hash Map | 39 ms ⏱️ (Beats 94.09%) | 16.96 MB 💡 (Beats 62.56%)
### Simple Explanation

### Intuition
To solve the problem of finding all paths in a binary tree where the sum of node values equals a given `targetSum`, the idea is to explore the tree while keeping track of the sum from the root to each node. We use a method called depth-first search (DFS) to explore all paths efficiently. A hash map helps us quickly check if any part of the path matches the `targetSum`.

### Approach
1. **DFS Traversal with Running Sum**:
   - Use DFS to explore the tree, keeping a running sum (`cursum`) as you move from the root to each node.
  
2. **Using a Hash Map (`prefsum`)**:
   - The hash map stores the sums we encounter during the traversal and how often each sum appears.
  
3. **Counting Valid Paths**:
   - For each node, check if there’s a previously seen sum that, when subtracted from the current sum, equals `targetSum`. If there is, it means there’s a valid path ending at that node.

4. **Backtracking**:
   - After processing a node and its children, undo the changes to the hash map (backtrack) to keep it relevant only to the current path.

### Complexity
- **Time Complexity**: \(O(N)\)
  - We visit each node in the tree once, so the time complexity is \(O(N)\), where \(N\) is the number of nodes.

- **Space Complexity**: \(O(H)\)
  - The space complexity is mainly due to the recursion stack, which is \(O(H)\) where \(H\) is the height of the tree. The hash map could take \(O(N)\) space if all nodes have unique sums.
  
### Code
'''
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right.

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, cursum):
            nonlocal count
            if not node:
                return
            
            cursum += node.val 

            # Count paths that end at the current node and sum to targetSum
            count += prefsum.get(cursum - targetSum, 0)

            # Update the hash map with the current sum
            prefsum[cursum] = prefsum.get(cursum, 0) + 1

            # Recursively process the left and right children
            dfs(node.left, cursum)
            dfs(node.right, cursum)

            # Backtrack: remove the current sum from the map
            prefsum[cursum] -= 1

        count = 0
        prefsum = {0: 1}  # Base case: to handle paths that sum exactly to targetSum
        dfs(root, 0)
        return count
```
