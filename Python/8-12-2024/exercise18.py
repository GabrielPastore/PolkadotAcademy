#Separate words from a string
from collections import Counter

def sep_str(x: str):
    spaces = Counter(x.lower())[" "]
    return x.split(" ", maxsplit=spaces)

def clean_str(words: list) -> list:
    for w in words:
        letter_absence = 0
        for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if letter not in w:
                letter_absence += 1
        if letter_absence == 26:    
            words.remove(w)
    return words

def main():
    string = input("Write a sentence.\nA: ")
    words = clean_str(sep_str(string))
    print(f"Your sentence has a total of {len(words)} words.")

main()