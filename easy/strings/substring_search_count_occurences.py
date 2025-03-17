"""
Given a string text and a substring pattern, count how many times pattern
appears in text.
"""

# text = "abababa"
# pattern = "aba"
# Output: 3

# text = "mississippi"
# pattern = "issi"
# Output: 2

text = "mississippi"
pattern = "issi"


def substring_search(text, pattern):
    count = 0
    i = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


print(substring_search(text, pattern))
