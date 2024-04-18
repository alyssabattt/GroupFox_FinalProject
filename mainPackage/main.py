import json

def decrypt_location(encrypted_indices, file_path):
    # Read the file and build a list of words
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Decrypt the message
    decrypted_message = []
    for index in encrypted_indices:
        line_number = int(index) - 1  # Adjust for zero-based index
        if 0 <= line_number < len(lines):
            decrypted_message.append(lines[line_number].strip())  # Strip newline characters
    
    return ' '.join(decrypted_message)

# Path to the JSON file with encrypted data
json_file_path = '../dataPackage/EncryptedGroupHints Spring 2024 Section 001-1 (1).json'

# Load encrypted indices for the 'Fox' group from the JSON file
with open(json_file_path, 'r') as json_file:
    encrypted_data = json.load(json_file)
    fox_group_encrypted_indices = encrypted_data['Fox']

# Path to the 'UCEnglish (1).txt' file
english_file_path = '../dataPackage/UCEnglish (1).txt'

# Decrypt the location for the 'Fox' group
decrypted_location = decrypt_location(fox_group_encrypted_indices, english_file_path)
print(decrypted_location)


