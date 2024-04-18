# main.py

from campusPackage.campus import *

if __name__ == "__main__":
    fox_words = decode_fox_category("UCEnglish.txt", "EncryptedGroupHints Spring 2024 Section 001-1.json")
    print("Our location on campus is:")
    print(' '.join(fox_words))
