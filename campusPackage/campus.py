#campus.py
'''*********************************************************************************************************************************
# Name: Anna Bowers, Alyssa Battaglia, Duncan Ward
# email: bowersas@mail.uc.edu, battagaa@mail.uc.edu, ward2dc@mail.uc.edu 
# Assignment Number: Final Project
# Due Date: 4/23/24
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is our final project for this class

# Citations: https://www.quora.com/How-do-you-print-an-image-with-code-on-Python, chat gpt "fix my indenting", 
https://claude.ai/chat/d278c76d-f5e5-4ff7-89eb-20529d9da606: prompt, solve error surroudning,
https://stackoverflow.com/questions/68823738/decrypting-a-json-dictionary-to-be-altered-python,
https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
# Anything else that's relevant: This was lowkey fun 
*********************************************************************************************************************************'''
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
    # Give us the location(s) on campus
    return decoded_words
