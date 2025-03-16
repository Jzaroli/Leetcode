"""
Given a string as a list of characters,
reverse the string in-place using the two-pointer approach.
"""

# Input: ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]

# Time Complexity: O(n) (swap each element once)
# Space Complexity: O(1) (modify the list in-place, no extra space used)

s = ["h", "e", "l", "l", "o", "1"]


def reverse_string(s: list) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap characters
        left += 1
        right -= 1  # Move pointers towards the center


reverse_string(s)
print(s)
