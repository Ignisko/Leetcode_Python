"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.class

"""
    def isPalindrome(self, s: str) -> bool:
        #conver upper into lower
        s = s.lower()
        #remove non-alphanumeric char
        s = ''.join(char for char in s.lower() if char.isalnum())
        #do sliding window to check
        e = 0 #ezker
        r = len(s) - 1  #right
        while e < r:
            if s[e] != s[r]:
                return False
            e += 1
            r -= 1
        return True
