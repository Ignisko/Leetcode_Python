'''

Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        def expand_around_center(left, right):
            nonlocal longest
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            current = s[left + 1:right]
            if len(current) > len(longest):
                longest = current

        for i in range(len(s)):
            expand_around_center(i, i)   # For odd-length palindromes
            expand_around_center(i, i + 1) # For even-length palindromes

        return longest
