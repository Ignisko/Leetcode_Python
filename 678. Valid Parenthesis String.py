
'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'. 

'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = max_open = 0
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open = max(min_open - 1, 0)
                max_open -= 1
                if max_open < 0:
                    # More closing parentheses than opening ones
                    return False
            else:  # char == '*'
                # Asterisk could be '(', ')', or ''
                min_open = max(min_open - 1, 0)
                max_open += 1
        
        # Valid if min_open is 0 (all open parentheses can be closed)
        return min_open == 0

