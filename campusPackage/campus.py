
#campus.py
import json

def decode_fox_category(english_file_path, json_file_path):
    with open(english_file_path, "r") as english_file:
        english_words = english_file.readlines()

    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        
    decoded_words = []
    fox_line_numbers = data.get("Fox", [])
    for line_number in fox_line_numbers:
        line_number = int(line_number)
        if 0 <= line_number < len(english_words):
            decoded_words.append(english_words[line_number].strip())

    return decoded_words
