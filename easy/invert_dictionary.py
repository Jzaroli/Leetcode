"""
Write a function that inverts a given dictionary.

The keys become values, and the values become keys.
Assume that all values in the original dictionary are unique.
"""

d = {"apple": "fruit", 
     "carrot": "vegetable", 
     "dog": "animal"
     }


def invert_dict(d: dict) -> dict:
    inv = {}
    for key, value in d.items():
        inv[value] = key
    return inv


b = invert_dict(d)
print(b)
