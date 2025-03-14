"""
Given two strings s and t, return True if t is an anagram of s,
and False otherwise.
"""

# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False

s = "anagram"
t = "nagaram"


def anagram(s, t):
    s_array = []
    t_array = []
    for letter in s:
        s_array.append(letter)
    for letter in t:
        t_array.append(letter)

    sorted_s = "".join(sorted(s_array))

    sorted_t = "".join(sorted(t_array))

    if sorted_s == sorted_t:
        return True
    else:
        return False


outcome = anagram(s, t)
print(outcome)


# Alternative: HashMap (More Efficient for Large Inputs)
"""
from collections import Counter

def anagram(s, t):
    return Counter(s) == Counter(t)  # Count letters in both strings
    and compare
"""


# Alternative: Manual HashMap (Without Counter):
"""
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}  # HashMap to store character frequencies
    for char in s:
        count[char] = count.get(char, 0) + 1  # Increase frequency

    for char in t:
        if char not in count or count[char] == 0:
            return False  # Character not found or frequency mismatch
        count[char] -= 1  # Decrease frequency

    return all(value == 0 for value in count.values())  # All frequencies
    should be zero
"""
