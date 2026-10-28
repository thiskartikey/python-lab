import sys

# Function to encrypt or decrypt text using Caesar Cipher
def caesar_cipher(message, shift_key):
    cipher_text = ""
    for char in message:
        if char.isupper():
            # Shift uppercase letters (A-Z)
            cipher_text += chr((ord(char) - ord('A') + shift_key) % 26 + ord('A'))
        elif char.islower():
            # Shift lowercase letters (a-z)
            cipher_text += chr((ord(char) - ord('a') + shift_key) % 26 + ord('a'))
        else:
            # Non-alphabetic characters remain untouched
            cipher_text += char
    return cipher_text

# Handle command-line arguments if provided
if len(sys.argv) >= 3:
    input_text = sys.argv[1]
    key = int(sys.argv[2])
    print("Encrypted:", caesar_cipher(input_text, key))
    print("Decrypted:", caesar_cipher(input_text, -key))
else:
    # Interactive user input mode
    input_text = input("Enter text: ")
    key = int(input("Enter shift value: "))
    user_choice = input("Enter E for Encryption or D for Decryption: ").strip().upper()

    if user_choice == "E":
        print("Encrypted:", caesar_cipher(input_text, key))
    elif user_choice == "D":
        print("Decrypted:", caesar_cipher(input_text, -key))
    else:
        print("Invalid choice!")
