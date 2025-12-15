from asr_irrelevant_word_fixing import process_sentence
from asr_spelling_mistake_fixing import correct_sentence
from asr_nid_card_related_word_fixing import replace_terms_in_sentence

def fix_transcription_output(sentence):
    # corrected_sentence = correct_sentence(sentence)
    # processed_sentence = process_sentence(corrected_sentence)
    # processed_sentence = replace_terms_in_sentence(processed_sentence)
    # processed_sentence = replace_terms_in_sentence(nid_related_word_fixed_sentence)
    corrected_sentence = correct_sentence(sentence)
    processed_sentence = process_sentence(corrected_sentence)
    # nid_related_word_fixed_sentence = replace_terms_in_sentence(processed_sentence)
    # processed_sentence = replace_terms_in_sentence(processed_sentence)
    return processed_sentence

    # return processed_sentence

# # Author: Ataullha Saim

# from asr_irrelevant_word_fixing import process_sentence
# from asr_spelling_mistake_fixing import correct_sentence
# from asr_nid_card_related_word_fixing import replace_terms_in_sentence

# def fix_transcription_output(sentence):
#     corrected_sentence = correct_sentence(sentence)
#     processed_sentence = process_sentence(corrected_sentence)
#     # nid_related_word_fixed_sentence = replace_terms_in_sentence(processed_sentence)
#     # processed_sentence = replace_terms_in_sentence(processed_sentence)
#     return processed_sentence
