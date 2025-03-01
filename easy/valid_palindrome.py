import re

# A phrase is a palindrome if it reads the same forward and backward, ignoring
# case, spaces, and non-alphanumeric characters.
# Write a function that returns True if a given string is a palindrome, and
# False otherwise

string = 'racecar'


def is_palindrome(stri):
    array = []

    for element in stri:
        array.append(element)

    array.reverse()
    reversed_stri = "".join(array)

    if stri == reversed_stri:
        print('The string is a palindrome')
        return True
    elif stri != reversed_stri:
        print('The string is not a palindrome')
        return False


is_palindrome(string)


# Advanced Solution:

def is_palindrome2(s: str) -> bool:
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Remove non-
    # alphanumeric characters & convert to lowercase
    return cleaned_str == cleaned_str[::-1]  # Check if it's a palindrome
    # using sequence[start:stop:step]


# Test cases
print(is_palindrome2("A man, a plan, a canal: Panama"))  # True
print(is_palindrome2("race a car"))  # False
