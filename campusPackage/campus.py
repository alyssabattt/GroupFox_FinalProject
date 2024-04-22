
#campus.py
import json

def decode_fox_category(english_file_path, json_file_path):
    '''
    Takes a text and json file and uses the json file numbers to decode the lines from the text file. Specific to the group Fox.
    @param: english_file_path: The txt file to use, json_file_path: the json file to use
    @return: decoded_words: the decoded message based on the two files.
    '''
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
