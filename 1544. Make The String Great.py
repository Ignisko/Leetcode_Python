'''
PROBLEM

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.

SOLUTION

Intuition
When I first saw the problem, it was clear that we needed to keep removing pairs of letters where one is just the uppercase version of the other, sitting side by side. I figured we'd need a way to easily add letters we're looking at and also quickly remove them if we find such a pair. That led me to think of using a stack, a simple tool that lets us put letters on top and also take them off from the top. This setup is perfect for checking the most recent letter against the new one we come across as we go through the string.

Approach
The approach involves iterating over each character in the string and using a stack to keep track of the characters processed. For each character:

If the stack is not empty and the current character forms a "bad" pair with the top character of the stack (i.e., they are the same letter in different cases), pop the top character off the stack, effectively removing both characters from the final string.
Otherwise, push the current character onto the stack.
After processing all characters, the stack will contain only the characters that should remain in the "good" string, in reverse order. Convert the stack back to a string by popping all characters and concatenating them in reverse order.

Complexity
Time Complexity: O(n)O(n)O(n), since we go through each letter once and stack actions are quick.
Space Complexity: O(n)O(n)O(n) in the worst case, if no pairs are removed; otherwise, less.

Codeclass Solution:
'''

    def makeGood(self, s: str) -> str:
        stack = []  # Using a list as a stack
        for c in s:
            # Check if the stack is not empty and the last character in the stack forms a bad pair with the current character
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()  # Remove the last character from the stack
            else:
                stack.append(c)  # Add the current character to the stack
        return ''.join(stack)  # Convert the stack back to a string and return
