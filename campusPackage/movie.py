#movie.py

#https://stackoverflow.com/questions/68823738/decrypting-a-json-dictionary-to-be-altered-python
#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/



from cryptography.fernet import Fernet
from mainPackage.main import *
#use this one 

key= bytes(b'')
filename='TeamsAndEncryptedMessagesForDistribution - 001.json'

def decrypt(key,filename):
    keyval=Fernet('KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE=')
    with open('TeamsAndEncryptedMessagesForDistribution - 001.json','rb') as f:
        #read encrypted data
        encrypted_data = f.rad()
        #decrypt data
        decrypted_data=dict(keyval.decrypt(encrypted_data))
        decrypted_data['rsi'][0]['tradingPair']='ETHUSD'
    decrypt('KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE=','TeamsAndEncryptedMessagesForDistribution - 001.json')
    
#     KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE=
