"""
Write a function that takes an unsigned integer and returns the number of 1
bits it has (also known as the Hamming weight).
"""

# n = 11  Binary: 1011
# output = 3  (because there are three '1' bits)


def hammingWeight(n):
    count = 0
    while n:
        n &= (n - 1)  # Removes the rightmost 1 bit
        count += 1
    return count


print(hammingWeight(11))  # Output: 3
