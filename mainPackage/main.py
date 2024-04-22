# main.py
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
# Anything else that's relevant: This was fun 
*********************************************************************************************************************************'''
from campusPackage.campus import *
from PIL import Image 
from campusPackage.movie import *

if __name__ == "__main__":
    # Print our movie quote
    print("May the force be with you")
    fox_words = decode_fox_category("UCEnglish.txt", "EncryptedGroupHints Spring 2024 Section 001-1.json")
    print("Our location on campus is:")
    print(' '.join(fox_words))
    # Show group picture at the Neil Armstrong exhibit
    image= Image.open('group_pic1.png')
    image.show()
    
