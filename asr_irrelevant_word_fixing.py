# Author: Ataullha Saim

from rapidfuzz import fuzz
from rapidfuzz import process

def process_sentence(sentence):
    # Define a list of greeting-related words
    greeting_words = ["আসসালামুয়ালাইকুম", "মুয়ালাইকুম", "আসসালাম", "ওয়ালাইকুম"]

    # Split the sentence into words
    words = sentence.split()

    # If the sentence has exactly 4 words, return it as is
    if len(words) < 4:
        return sentence

    # Check the first two words
    filtered_words = []
    for word in words[:2]:
        # Use fuzzy matching to check similarity with greeting words
        match = process.extractOne(word, greeting_words, scorer=fuzz.ratio)
        if match and match[1] < 80:  # Keep the word if it's not similar to a greeting word
            filtered_words.append(word)

    # Add the rest of the sentence after the first two words
    filtered_words.extend(words[2:])

    # Join and return the filtered sentence
    return ' '.join(filtered_words)