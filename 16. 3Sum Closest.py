'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], tgt: int) -> int:
        nums.sort()
        closest = float('inf')
        

        for i in range(len(nums) - 2):
            l, r =  i + 1, len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - tgt) < abs(closest - tgt):
                    closest = curr_sum

                if curr_sum < tgt:
                    l += 1
                elif curr_sum > tgt:
                    r -= 1
                else:
                    return curr_sum
        
        return closest


