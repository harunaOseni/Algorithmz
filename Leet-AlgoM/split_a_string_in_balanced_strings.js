// SPLIT A STRING IN BALANCED STRINGS

// Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

// Given a balanced string s, split it in the maximum amount of balanced strings.

// Return the maximum amount of split balanced strings.

// Example 1:

// Input: s = "RLRRLLRLRL"
// Output: 4
// Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
// Example 2:

// Input: s = "RLLLLRRRLR"
// Output: 3
// Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
// Example 3:

// Input: s = "LLLLRRRR"
// Output: 1
// Explanation: s can be split into "LLLLRRRR".
// Example 4:

// Input: s = "RLRRRLLRLL"
// Output: 2
// Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

// Constraints:

// 1 <= s.length <= 1000
// s[i] is either 'L' or 'R'.
// s is a balanced string.

//Time Complexity - O(n)
//Space Complexity - O(1)

/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
  let result = 0;
  //RL RRLL RL RL
  //1   2    3  4

  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "R") {
      count++;
    } else {
      count--;
    }

    if (count === 0) {
      result++;
    }
  }

  return result;
};
