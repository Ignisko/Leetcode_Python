'''
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.

Hint 1
Represent the counts (odd or even) of vowels with a bitmask.
Hint 2
Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.

'''
#sol 1: bitmask
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        mask = 0
        res = 0

        vow = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        for i, ch in enumerate(s):
            if ch in vow:
                mask ^= vow[ch]

            if mask in seen:
                res = max(res, i - seen[mask])
            else:
                seen[mask] = i
        
        return res


#sol 2: greedy algorithm
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        count = Counter(s)
        n = len(s)
        rev = True

        for l in range(n, 0, -1):
            if all(count[v] % 2 == 0 for v in "aeiou"):
                return l

            if rev:
                count[s[l-1]] -= 1
                e = range(n - l + 1)
                r = range(l - 1, n)
            else:
                count[s[-l]] -= 1
                e = reversed(range(l - 1, n))
                r = reversed(range(n - l + 1))

            if all(count[v] % 2 == 0 for v in "aeiou"):
                return l - 1

            for i, j in zip(e, r):
                count[s[i]] -= 1
                count[s[j]] += 1
                if all(count[v] % 2 == 0 for v in "aeiou"):
                    return l - 1

            rev = not rev
        
        return 0

