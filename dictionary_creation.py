
# import functions
import csv
import json

# imports for english, russian, and spanish
import add_english
import add_russian
from add_russian import test_russian_dict
from add_spanish import test_spanish_dict

# import new alphabet
#import assign_new_alphabet

# the nested list for the new dictionary
new_dict = []

def english_to_russian(english_words, test_russian_dict):
    for eng_word, eng_def in english_words:
        match_found = False
        for rus_word, rus_def in test_russian_dict.items():
            # Naive match: if a Russian definition contains an English definition keyword
            # please add more stipulations this is terrible
            
            if eng_def.lower().split()[0] in rus_def.lower():
                # Add the shorter word to the new dictionary
                shorter_word = eng_word if len(eng_word) < len(rus_word) else rus_word
                new_dict.append((shorter_word, eng_def))
                match_found = True
                break
        
        if not match_found:
            # No match found: just keep the English word as-is (for now)
            new_dict.append((eng_word, eng_def))
        
    # compares / searches for direct translation, then creates new word
    # if definition of a word is the same and length of word is different:
        # then select the shorter word
#        new_dict.append((word, definition))
    # elif definition is the same and word length is the same:
        # then select spanish equivalent
        # get root word from english or russian at random and swap it from spanish
    # elif definition is not the same or its not a direct translation:
        # keep the origional word as is (for now)
    # elif 

def russian_to_english(russian_words, english_dict):
    # same shit just skip over words already added to new_dict
    for rus_word, rus_def in russian_words:
        match_found = False
        for eng_word, eng_def in test_russian_dict.items():
            # Naive match: if a Russian definition contains an English definition keyword
            # please add more stipulations this is terrible
            
            if rus_def.lower().split()[0] in eng_def.lower():
                # Add the shorter word to the new dictionary
                shorter_word = rus_word if len(rus_word) < len(eng_word) else eng_word
                new_dict.append((shorter_word, eng_def))
                match_found = True
                break
        
        if not match_found:
            # No match found: just keep the English word as-is (for now)
            new_dict.append((rus_word, rus_def))

def assign_alphabet(new_dict):
    # learn the LaTex thing first, good luck ig

# main
english_words = add_english.load_english_dictionary(r"C:\Users\leahe\Downloads\Artificial Language\dictionary.json")

# Example usage
for word, definition in english_words[:10]:  # Show first 10 for testing
    print(word, ":", definition)

english_to_russian(english_words[:10], test_russian_dict)

# See the new dictionary output
for word, definition in new_dict:
    print(word, "->", definition)
