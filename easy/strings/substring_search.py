"""
Implement the strStr() function.
Given two strings haystack and needle, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.
Constraints:
Return 0 if needle is an empty string ("").
You cannot use Python's built-in find() or index() methods.
"""

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Input: haystack = "leetcode", needle = ""
# Output: 0

haystack = "hello"
needle = "ll"


def strStr(haystack, needle):
    i = 0
    if needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


output = strStr(haystack, needle)
print(output)
