"""
The Roman numeral system uses seven symbols:
I (1), V (5), X (10), L (50), C (100), D (500), M (1000).
To convert a Roman numeral to an integer, we use two rules:
If a smaller value is before a larger value, subtract it (e.g., IV = 4,
IX = 9).
Otherwise, add the value (e.g., VI = 6, XII = 12).
"""

"""
Given a string s representing a Roman numeral, convert it to an integer.
"""

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M (1000) + CM (900) + XC (90) + IV (4) = 1994

s = "MCMXCIV"


def romanToInt(s):
    i = 0
    count = 0
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    for i in range(len(s) - 1):
        if romans[s[i]] < romans[s[i + 1]]:
            count -= romans[s[i]]
        else:
            count += romans[s[i]]
    count += romans[s[-1]]
    return count


print(romanToInt(s))
