"""
Given an integer array nums, return True if any value appears at least twice,
and False if all elements are unique.
"""

# Input: nums = [1,2,3,1]
# Output: True

# Input: nums = [1,2,3,4]
# Output: False

nums = [1, 2, 3, 1]


def is_dupe(nums):
    verify = set()
    nums_set = set(nums)
    for num in nums:
        if num not in verify:
            verify.add(num)
    if verify == nums_set:
        return True
    else:
        return False


output = is_dupe(nums)
print(output)


"""
SOLUTION:

def is_dupe(nums):
    seen = set()  # To track numbers we've seen so far
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
    return False  # No duplicates

# Example usage:
nums = [1, 2, 3, 1]
output = is_dupe(nums)
print(output)  # Output: True
"""
