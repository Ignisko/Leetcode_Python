
'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
232.1K
Submissions
329.5K
Acceptance Rate
70.4%
Topics
Companies
Hint 1
We can use nested loops to compare every row against every column.
Hint 2
Another loop is necessary to compare the row and column element by element.
Hint 3
It is also possible to hash the arrays and compare the hashed values instead.

'''
#1 
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowct = defaultdict(int)

        for row in grid:
            rowct[tuple(row)] += 1

        ct = 0

        for colidx in range(n):
            col = tuple(grid[rowidx][colidx] for rowidx in range(n))
            if col in rowct:
                ct += rowct[col]
        
        return ct

#---------------------------------------------------------------------------------------------
# 2, slightly slower but less memory, not a big difference
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowct = Counter(tuple(row) for row in grid)
        pairct = 0

        for col in zip(*grid):
            pairct += rowct[tuple(col)]
        
        return pairct
      
