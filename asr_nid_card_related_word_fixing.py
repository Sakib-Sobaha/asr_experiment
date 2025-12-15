import Levenshtein

# Example usage dictionary
incorrect_to_correct = {
    'নেডিকাইটি': 'এনআইডি',
    'গার্ড': 'কার্ড',
    'এনেডি': 'এনআইডি',
    'এনাডিকাটে': 'এনআইডি',
    'রডি': 'কার্ড',
    'অ্যানেডিকার্ডের': 'এনআইডি কার্ড',
    'এনাইডিকাট': 'এনআইডি',
    'এনেইডিকেট': 'এনআইডি',
    'নেডিকাট': 'এনআইডি',
    'এন্দিকারড': 'এনআইডি কার্ড',
    'এনএডিকেটে': 'এনআইডি',
    'এনআইডকার্ড': 'এনআইডি কার্ড',
    'নেডিকার্ডসহ': 'এনআইডি কার্ড',
    'এনাডিকার্ডে': 'এনআইডি কার্ড',
    'অ্যানি রিকার্ড': 'এনআইডি কার্ড',
    'আইডিকেড': 'এনআইডি',
    'অ্যানেডি গার্ডে': 'এনআইডি কার্ড',
    'অ্যানেইডিকাট': 'এনআইডি',
    'অ্যানাইডি': 'এনআইডি',
    'এনআইডিকারেডে': 'এনআইডি কার্ড',
    'গার্ডে': 'কার্ড',
    'এনআইরি': 'এনআইডি',
    'কার্নে': 'কার্ড',
    'এনেডিকার্নে': 'এনআইডি কার্ড',
    'এনআইডিকার্টে': 'এনআইডি কার্ড',
    'কার্ট': 'কার্ড',
    'কার্টে': 'কার্ডে',
    'নেডিকায়ডে': 'এনআইডি',
    'আগযে': 'এনআইডি',
    'সিগন্যাচাকটা': 'এনআইডি কার্ড',
    'এনেডিকার্ডের': 'এনআইডি কার্ড',
    'অ্যানেডিকাট': 'এনআইডি',
    'এনাইডিকারেটে': 'এনআইডি',
    'এনেডিকাররে': 'এনআইডি',
    'নিন্দির': 'এনআইডির',
    'কারড়ির': 'কার্ডের',
    'কার্গে ': 'কার্ডে'
}

def replace_terms_in_sentence(sentence, incorrect_to_correct=incorrect_to_correct, threshold=2):
    words = sentence.split()
    corrected_words = []
    
    for word in words:
        # Check for closest match using Levenshtein distance to dictionary keys
        closest_match = min(incorrect_to_correct.keys(), key=lambda key: Levenshtein.distance(word, key))
        distance = Levenshtein.distance(word, closest_match)
        
        # If the distance is below the threshold, replace the word with the mapped value
        if distance <= threshold:
            corrected_words.append(incorrect_to_correct[closest_match])
        else:
            corrected_words.append(word)

    # Join the corrected words back into a sentence
    corrected_sentence = ' '.join(corrected_words)
    return corrected_sentence
    
# import Levenshtein

# # Example usage dictionary
# incorrect_to_correct = {
#     'নেডিকাইটি': 'এনআইডি',
#     'গার্ড': 'কার্ড',
#     'এনেডি': 'এনআইডি',
#     'এনাডিকাটে': 'এনআইডি',
#     'রডি': 'কার্ড',
#     'অ্যানেডিকার্ডের': 'এনআইডি কার্ড',
#     'এনাইডিকাট': 'এনআইডি',
#     'এনেইডিকেট': 'এনআইডি',
#     'নেডিকাট': 'এনআইডি',
#     'এন্দিকারড': 'এনআইডি কার্ড',
#     'এনএডিকেটে': 'এনআইডি',
#     'এনআইডকার্ড': 'এনআইডি কার্ড',
#     'নেডিকার্ডসহ': 'এনআইডি কার্ড',
#     'এনাডিকার্ডে': 'এনআইডি কার্ড',
#     'অ্যানি রিকার্ড': 'এনআইডি কার্ড',
#     'আইডিকেড': 'এনআইডি',
#     'অ্যানেডি গার্ডে': 'এনআইডি কার্ড',
#     'অ্যানেইডিকাট': 'এনআইডি',
#     'অ্যানাইডি': 'এনআইডি',
#     'এনআইডিকারেডে': 'এনআইডি কার্ড',
#     'গার্ডে': 'কার্ড',
#     'এনআইরি': 'এনআইডি',
#     'কার্নে': 'কার্ড',
#     'এনেডিকার্নে': 'এনআইডি কার্ড',
#     'এনআইডিকার্টে': 'এনআইডি কার্ড',
#     'কার্টে': 'কার্ড',
#     'নেডিকায়ডে': 'এনআইডি',
#     'আগযে': 'এনআইডি',
#     'সিগন্যাচাকটা': 'এনআইডি কার্ড',
#     'এনেডিকার্ডের': 'এনআইডি কার্ড',
#     'অ্যানেডিকাট': 'এনআইডি',
#     'এনাইডিকারেটে': 'এনআইডি',
#     'এনেডিকাররে': 'এনআইডি'
# }

# def replace_terms_in_sentence(sentence, incorrect_to_correct=incorrect_to_correct, threshold=2):
#     words = sentence.split()
#     corrected_words = []
    
#     for word in words:
#         # Check for closest match using Levenshtein distance to dictionary keys
#         closest_match = min(incorrect_to_correct.keys(), key=lambda key: Levenshtein.distance(word, key))
#         distance = Levenshtein.distance(word, closest_match)
        
#         # If the distance is below the threshold, replace the word with the mapped value
#         if distance <= threshold:
#             corrected_words.append(incorrect_to_correct[closest_match])
#         else:
#             corrected_words.append(word)

#     # Join the corrected words back into a sentence
#     corrected_sentence = ' '.join(corrected_words)
#     return corrected_sentence

# # # Example usage
# # sentence = 'নেডিকাইটি গার্ড এনেডি'
# # corrected_sentence = replace_terms_in_sentence(sentence)
# # print(corrected_sentence)
