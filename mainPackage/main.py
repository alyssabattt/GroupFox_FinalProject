# main.py

#https://www.quora.com/How-do-you-print-an-image-with-code-on-Python


from campusPackage.campus import *
from PIL import Image 
from campusPackage.movie import *

if __name__ == "__main__":
    fox_words = decode_fox_category("UCEnglish.txt", "EncryptedGroupHints Spring 2024 Section 001-1.json")
    print("Our location on campus is:")
    print(' '.join(fox_words))
    image= Image.open('groupPic.png')
    image.show()
    
