#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re
import string

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        user_sentence = input("Enter a sentence: ")

        if is_sentence(user_sentence):
            return user_sentence
        else:
            print("This does not meet the criteria for a sentence.")

def calculate_frequencies(sentence):
    cleaned_words = sentence.lower()translate(
        str.maketrans('', '', string.punctuation)
    ).split()

    words = []
    frequencies = []

    for w in cleaned_words:
        if w:
            if w not in words:
                words.append(w)
                frequencies.append(1)
            else:
                frequencies[words.index(w)] += 1

    return words, frequencies

def print_frequencies(words, frequencies):
    print("--- Word Frequencies ---")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence_string = get_sentence()
    words, frequencies = calculate_frequencies(sentence_string)
    print_frequencies(words, frequencies)

if __name__ == "__main__":
    main()
        
