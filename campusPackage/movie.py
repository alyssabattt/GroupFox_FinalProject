#movie.py
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
https://courses.cs.washington.edu/courses/cse140/13wi/file-interaction.html#:~:text=Absolute%20and%20Relative%20file%20paths&text=An%20absolute%20file%20path%20describes,For%20example%2C%20example_directory.
# Anything else that's relevant: This was lowkey fun 
*********************************************************************************************************************************'''
import json
from cryptography.fernet import Fernet
from mainPackage.main import *

key = "KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE="
# Loading the encrypted messages from a JSON file.
with open("TeamsAndEncryptedMessagesForDistribution - 001.json", "r") as file:
    data = json.load(file)

# Initialize the Fernet class with the provided key for the decryption process.
fernet = Fernet(key)
team = "Fox"
if team in data:
    messages = data[team]
    decrypted_messages = []
    for encrypted_message in messages:
            # Decode each message from base64, decrypt, and convert from bytes to string.
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            decrypted_messages.append(decrypted_message)
    data[team] = decrypted_messages
    for message in data[team]:
        # Give us our movie title
        print(f"Team foxes movie is: {message}")
