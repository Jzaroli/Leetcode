import re
"""
Write a function that takes a string s and returns a dictionary where the keys
are words in the string and the values are the number of times
each word appears.

The function should ignore capitalization (treat "Hello" and "hello" as
the same word).
Remove punctuation.
Words are separated by spaces.
"""
s = "Python is fun. Python, Python, Python!"


def word_count(s: str) -> dict:
    word_dict = {}
    s2 = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower()
    words = s2.split(' ')

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


print(word_count("Hello world! Hello again, world."))
print(word_count("Python is fun. Python, Python, Python!"))


""" Alternative:

from collections import Counter
import re

def word_count(s: str) -> dict:
    cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower()
    words = cleaned_str.split()
    return dict(Counter(words))  # Automatically counts occurrences

print(word_count("Hello world! Hello again, world."))
"""
