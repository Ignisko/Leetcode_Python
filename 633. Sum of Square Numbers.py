'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
'''
class Solution(object):
    def judgeSquareSum(self, c):
        a = 0
        b = int(math.sqrt(c))

        while a <= b: 
            sum1 = a * a + b * b
            if sum1 == c: 
                return True
            elif sum1 < c:
                a += 1
            else: 
                b -= 1
        return False
