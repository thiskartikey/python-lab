import sys

def caesar_cipher(message, shift_key):
    cipher_text = ""
    for char in message:
        if char.isupper():
            cipher_text += chr((ord(char) - ord('A') + shift_key) % 26 + ord('A'))
        elif char.islower():
            cipher_text += chr((ord(char) - ord('a') + shift_key) % 26 + ord('a'))
        else:
            cipher_text += char
    return cipher_text

if len(sys.argv) >= 3:
    input_text = sys.argv[1]
    key = int(sys.argv[2])
    print("Encrypted:", caesar_cipher(input_text, key))
    print("Decrypted:", caesar_cipher(input_text, -key))
else:
    input_text = input("Enter text: ")
    key = int(input("Enter shift value: "))
    user_choice = input("Enter E for Encryption or D for Decryption: ").strip().upper()

    if user_choice == "E":
        print("Encrypted:", caesar_cipher(input_text, key))
    elif user_choice == "D":
        print("Decrypted:", caesar_cipher(input_text, -key))
    else:
        print("Invalid choice!")
