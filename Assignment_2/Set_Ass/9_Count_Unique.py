# 9. Write a program to count the number of unique words in a sentence.
from collections import Counter

sentence = "The quick brown fox jumps over the lazy dog the quick brown fox"

words = sentence.lower().split()

unique_words = set(words)

unique_count = len(unique_words)

print("Original Sentence:", sentence)
print("Unique Words:", unique_words)
print("Total number of unique words:", unique_count)
