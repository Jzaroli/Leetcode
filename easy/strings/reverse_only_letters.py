"""
Given a string s, reverse only the letters, keeping non-letter
characters in place.
"""

# Input: s = "ab-cd"
# Output: "dc-ba"

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-Leet=gnsT-T!"

s = "Test1ng-Leet=code-Q!"


def reverseOnlyLetters(s):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s_l = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s_l[left] in letters and s_l[right] in letters:
            s_l[left], s_l[right] = s_l[right], s_l[left]
            left += 1
            right -= 1
        elif s_l[left] not in letters and s_l[right] in letters:
            left += 1
        elif s_l[left] in letters and s_l[right] not in letters:
            right -= 1
        elif s_l[left] not in letters and s_l[right] not in letters:
            left += 1
            right -= 1

    return "".join(s_l)


print(s)
print(reverseOnlyLetters(s))

# can use the isAlpha() method to simpligy the above
