# VALID PARENTHESIS

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Solution
# Time: O(n)
# Space: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_table = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        stack = []
        for parenthesis in s:
            if parenthesis in hash_table:
                stack.append(parenthesis)
            else:
                if not stack:
                    return False
                pop_value = stack.pop()
                if hash_table[pop_value] != parenthesis:
                    return False

        return len(stack) == 0