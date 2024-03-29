# CLIMBING STAIRS

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Constraints:

# 1 <= n <= 45

def climbStairs(n):
    step = [1, 1]

    for i in range(2, n+1):
        step.insert(i, step[i - 1] + step[i - 2])

    return step[n]


print(climbStairs(3))

# Rewrite for mastery 1:


def climbStairs(n):
    if (n == 1):
        return 1

    first = 1
    second = 2

    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second

# Rewrite for mastery 2:


def climbStairs(n):
    if (n == 1):
        return 1

    first = 1
    second = 2

    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second
