'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        e, r = 0, len(s) - 1 #ezker, right

        while e < r:
            if s[e] not in vowels:
                e += 1
                continue
            if s[r] not in vowels:
                r -= 1
                continue
            s[e], s[r] = s[r], s[e]
            e += 1
            r -= 1
        
        return ''.join(s)

