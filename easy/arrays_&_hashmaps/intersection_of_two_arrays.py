"""
Given two integer arrays nums1 and nums2, return an array of their
intersection.
Each element in the result must be unique, and you may return the result
in any order.
"""

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]


# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]


def intersection(arr1, arr2):
    nums1_set = set(arr1)
    nums2_set = set(arr2)
    final = []
    for num in nums1_set:
        if num in nums2_set:
            final.append(num)
    return final


final = intersection(nums1, nums2)
print(final)


"""
Optimized
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(intersection(nums1, nums2))  # Output: [9, 4]
"""
