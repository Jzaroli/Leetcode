"""
Given a sentence (a string) and a word (substring), find the index of the
first occurrence of the word in the sentence. If the word is not present,
return -1.
"""

# sentence = "The quick brown fox jumps over the lazy dog"
# word = "fox"
# Output: 16


sentence = "The quick brown fox jumps over the lazy dog"
word = "fox"


def substring_search(sentence, word):
    i = 0
    for i in range(len(sentence) - len(word) + 1):
        if sentence[i:i+len(word)] == word:
            return i
    return -1


print(substring_search(sentence, word))
