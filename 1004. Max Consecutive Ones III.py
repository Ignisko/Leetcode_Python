'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
#2

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        e = 0

        for i in nums:
            k += i - 1
            if k < 0:
                k += 1 - nums[e]
                e += 1
        
        return len(nums) - e

'''
#1
def longestOnes(self, nums: List[int], k: int) -> int:
        e = 0
        maxlen = 0
        zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
        
            while zeros > k:
                if nums[e] == 0:
                    zeros -= 1
                e += 1
        
            maxlen = max(maxlen, r - e + 1)
        
        return maxlen
