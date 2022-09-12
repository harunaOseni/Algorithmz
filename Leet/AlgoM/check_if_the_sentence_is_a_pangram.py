# CHECK IF THE SENTENCE IS A PANGRAM

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false

# Constraints:

# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

# Time: O(n)
# Space: O(1)

class Solution:
    def checkIfPangram(self, sentence):
        alphabet = [chr(i) for i in range(97, 123)]
        for i in alphabet:
            if i not in sentence:
                return False
        return True