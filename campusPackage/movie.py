#movie.py

#https://stackoverflow.com/questions/68823738/decrypting-a-json-dictionary-to-be-altered-python
#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
#https://claude.ai/chat/d278c76d-f5e5-4ff7-89eb-20529d9da606: prompt, solve error surroudning 


import json
from cryptography.fernet import Fernet
from mainPackage.main import *

key = "KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE="
with open("TeamsAndEncryptedMessagesForDistribution - 001.json", "r") as file:
    data = json.load(file)

fernet = Fernet(key)
team = "Fox"
if team in data:
    messages = data[team]
    decrypted_messages = []
    for encrypted_message in messages:
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            decrypted_messages.append(decrypted_message)
    data[team] = decrypted_messages
    for message in data[team]:
        print(f"Team foxes movie is: {message}")
