"""
A number is a power of two if it can be written as 2^x,
where x is a non-negative integer.
1 = 2^0
2 = 2^1
4 = 2^2
8 = 2^3
10 (not a power of two)
"""


# Input: n = 16
# Output: True
# Explanation: 16 = 2^4

# Input: n = 10
# Output: False
# Explanation: 10 is not a power of two.

def power_two(n):
    return n > 0 and (n & (n - 1)) == 0

# n & (n - 1) removes the rightmost set bit.
# If a number is a power of two, it only has one set bit, so the result is 0.
# A power of two has exactly one bit set in its binary representation.
# For example:
# 8 (1000 in binary) True
# 16 (10000 in binary) True
# 10 (1010 in binary) False
