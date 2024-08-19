
'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

Hint 1
Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.

Hint 2
Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].

'''
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = dict()
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        
        # If n is already in the memo, return it immediately
        if n in memo:
            return memo[n]
        
        # Iteratively compute the tribonacci number
        for i in range(3, n + 1):
            # Compute and store the tribonacci number
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
            # Remove the oldest memo value to save space
            del memo[i - 3]
            
        return memo[n]
