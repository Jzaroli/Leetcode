"""
Given a string s, reverse only the vowels (a, e, i, o, u) while keeping
the rest of the characters unchanged.
"""

# Input: string = "hello"
# Output: "holle"

# Input: string = "leetcode"
# Output: "leotcede"

string = "leetcode"


def reverseVowels(string):
    vowels = "aeiouyAEIOUY"
    s = list(string)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels and s[right] in vowels:
            left += 1
        elif s[left] in vowels and s[right] not in vowels:
            right -= 1
        elif s[left] not in vowels and s[right] not in vowels:
            left += 1
            right -= 1
    output = "".join(s)
    return output


output = reverseVowels(string)
print(output)


# Time Complexity
# O(n) — Each character is checked at most once.
# O(1) Extra Space — The list s is modified in-place.
