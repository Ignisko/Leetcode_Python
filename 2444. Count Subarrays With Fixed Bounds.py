from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0  # Counts the number of valid subarrays
        lastMin = -1  # Last position of minK
        lastMax = -1  # Last position of maxK
        left = -1  # Last position where the subarray would be invalid
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # If the current number is out of bounds, update the last invalid position
            if num < minK or num > maxK:
                left = i
            
            # Update the last positions of minK and maxK as we find them
            if num == minK:
                lastMin = i
            if num == maxK:
                lastMax = i
            
           
            if lastMin != -1 and lastMax != -1:
                count += max(0, min(lastMin, lastMax) - left)
        
        return count
