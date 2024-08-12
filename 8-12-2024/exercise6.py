#Count the vowels of a string
from collections import Counter

def vowel_count(x: str) -> int:
    c = Counter(x.lower())
    total = 0
    for e in "aeiou":
        total += c[e]
    return total

sentence = input("Enter a sentence.\nA: ")
print(f"Your sentence has {vowel_count(sentence)} vowels.")