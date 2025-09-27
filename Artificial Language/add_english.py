import json

def load_english_dictionary(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        english_dict = json.load(file)

    # Make sure to RETURN this list!
    return [(word, definition.strip()) for word, definition in english_dict.items()]
