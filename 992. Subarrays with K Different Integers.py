from collections import Counter
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            count = left = 0
            freq = Counter()
            for right, value in enumerate(nums):
                if freq[value] == 0:
                    k -= 1
                freq[value] += 1
                while k < 0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        k += 1
                    left += 1
                count += right - left + 1
            return count

        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
