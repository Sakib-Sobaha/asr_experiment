# Author: Ataullah Saim

import difflib
from collections import Counter

# Bangla dictionary of valid words with their frequencies
bangla_dict = {
    "আসসালামুয়ালাইকুম": 200,
    "মুয়ালাইকুম": 20,
    "আসসালাম": 20,
    "এনআইডি": 20,
    "অ্যানআইডি": 20
}


# Function to find the closest match from the dictionary based on frequency
def find_closest(word, dictionary):
    closest_matches = difflib.get_close_matches(
        word, dictionary.keys(), n=1, cutoff=0.5
    )
    if closest_matches:
        return max(
            closest_matches, key=lambda w: dictionary[w]
        )  # Return the most frequent match
    return word


# Function to split merged words
def split_merged_word(word, dictionary):
    for i in range(1, len(word)):
        part1, part2 = word[:i], word[i:]
        if part1 in dictionary and part2 in dictionary:
            return [part1, part2]  # Return split parts as a list
    return [word]  # Return the original word if no valid split is found


# Function to merge split words
def merge_split_words(words, dictionary):
    merged_sentence = []
    i = 0
    while i < len(words):
        if i < len(words) - 1:
            merged = words[i] + words[i + 1]
            if merged in dictionary:
                merged_sentence.append(merged)
                i += 2  # Skip the next word as it's merged
                continue
        merged_sentence.append(words[i])
        i += 1
    return merged_sentence


# Main function to correct, split, and merge
# def correct_sentence(sentence, dictionary):
#     # Step 1: Tokenize the sentence
#     words = sentence.split()

#     # Step 2: Correct individual words
#     corrected_words = [find_closest(word, dictionary) for word in words]

#     # Step 3: Handle splitting of merged words
#     split_words = []
#     for word in corrected_words:
#         split_words.extend(split_merged_word(word, dictionary))

#     # Step 4: Merge split words
#     final_words = merge_split_words(split_words, dictionary)

#     # Reconstruct the sentence
#     corrected_sentence = " ".join(final_words)
#     return corrected_sentence

# Function to check and clean greetings based on advanced rules
def clean_greeting(words, dictionary):
    # List of words related to greetings
    greeting_words = {"আসসালাম", "ওয়ালাইকুম", "মুয়ালাইকুম", "সালাম", "আসসালামুয়ালাইকুম"}
    
    # Step 1: Check first three or four words for greetings
    if len(words) >= 3:
        to_check = words[:4]  # Take the first 3-4 words

        # Step 2: Check if they match greeting patterns using fuzzy matching
        matched_words = [word for word in to_check if word in greeting_words]

        if matched_words:
            # Remove all words beyond greeting-related words in the first three or four words
            return matched_words + words[4:]  # Keep greetings and the rest of the sentence

    return words

# Main function to correct, split, and merge
def correct_sentence(sentence, dictionary=bangla_dict):
    # Step 1: Tokenize the sentence
    words = sentence.split()

    # Step 2: Correct individual words
    corrected_words = [find_closest(word, dictionary) for word in words]

    # Step 3: Handle splitting of merged words
    split_words = []
    for word in corrected_words:
        split_words.extend(split_merged_word(word, dictionary))

    # Step 4: Merge split words
    final_words = merge_split_words(split_words, dictionary)

    # Step 5: Clean greeting-related words
    cleaned_words = clean_greeting(final_words, dictionary)

    # Reconstruct the sentence
    corrected_sentence = " ".join(cleaned_words)
    return corrected_sentence

# # Author: Ataullah Saim

# import difflib
# from collections import Counter

# # Bangla dictionary of valid words with their frequencies
# bangla_dict = {
#     "আসসালামুয়ালাইকুম": 200,
#     "মুয়ালাইকুম": 20,
#     "আসসালাম": 20,
#     "এনআইডি": 20,
#     "অ্যানআইডি": 20
# }


# # Function to find the closest match from the dictionary based on frequency
# def find_closest(word, dictionary):
#     closest_matches = difflib.get_close_matches(
#         word, dictionary.keys(), n=1, cutoff=0.5
#     )
#     if closest_matches:
#         return max(
#             closest_matches, key=lambda w: dictionary[w]
#         )  # Return the most frequent match
#     return word


# # Function to split merged words
# def split_merged_word(word, dictionary):
#     for i in range(1, len(word)):
#         part1, part2 = word[:i], word[i:]
#         if part1 in dictionary and part2 in dictionary:
#             return [part1, part2]  # Return split parts as a list
#     return [word]  # Return the original word if no valid split is found


# # Function to merge split words
# def merge_split_words(words, dictionary):
#     merged_sentence = []
#     i = 0
#     while i < len(words):
#         if i < len(words) - 1:
#             merged = words[i] + words[i + 1]
#             if merged in dictionary:
#                 merged_sentence.append(merged)
#                 i += 2  # Skip the next word as it's merged
#                 continue
#         merged_sentence.append(words[i])
#         i += 1
#     return merged_sentence


# # Main function to correct, split, and merge
# def correct_sentence(sentence, dictionary):
#     # Step 1: Tokenize the sentence
#     words = sentence.split()

#     # Step 2: Correct individual words
#     corrected_words = [find_closest(word, dictionary) for word in words]

#     # Step 3: Handle splitting of merged words
#     split_words = []
#     for word in corrected_words:
#         split_words.extend(split_merged_word(word, dictionary))

#     # Step 4: Merge split words
#     final_words = merge_split_words(split_words, dictionary)

#     # Reconstruct the sentence
#     corrected_sentence = " ".join(final_words)
#     return corrected_sentence

# # Function to check and clean greetings based on advanced rules
# def clean_greeting(words, dictionary):
#     # List of words related to greetings
#     greeting_words = {"আসসালাম", "ওয়ালাইকুম", "মুয়ালাইকুম", "সালাম", "আসসালামুয়ালাইকুম"}
    
#     # Step 1: Check first three or four words for greetings
#     if len(words) >= 3:
#         to_check = words[:4]  # Take the first 3-4 words

#         # Step 2: Check if they match greeting patterns using fuzzy matching
#         matched_words = [word for word in to_check if word in greeting_words]

#         if matched_words:
#             # Remove all words beyond greeting-related words in the first three or four words
#             return matched_words + words[4:]  # Keep greetings and the rest of the sentence

#     return words

# # Main function to correct, split, and merge
# def correct_sentence(sentence, dictionary=bangla_dict):
#     # Step 1: Tokenize the sentence
#     words = sentence.split()

#     # Step 2: Correct individual words
#     corrected_words = [find_closest(word, dictionary) for word in words]

#     # Step 3: Handle splitting of merged words
#     split_words = []
#     for word in corrected_words:
#         split_words.extend(split_merged_word(word, dictionary))

#     # Step 4: Merge split words
#     final_words = merge_split_words(split_words, dictionary)

#     # Step 5: Clean greeting-related words
#     cleaned_words = clean_greeting(final_words, dictionary)

#     # Reconstruct the sentence
#     corrected_sentence = " ".join(cleaned_words)
#     return corrected_sentence
