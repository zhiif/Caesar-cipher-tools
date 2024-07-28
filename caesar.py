# caesar_cipher.py

import argparse
from colorama import Fore, Style, init

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    init(autoreset=True)
    ascii_art = f"""
{Fore.GREEN}   ░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
   ░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
   ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀    
    """
    print(ascii_art)
    print(Fore.BLUE + "Welcome to Caesar Cipher Tool" + Style.DIM)

    parser = argparse.ArgumentParser(description="Caesar Cipher Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose whether to encrypt or decrypt the text")
    parser.add_argument("text", help="The text to encrypt or decrypt")
    args = parser.parse_args()

    if args.mode == "encrypt":
        print(Fore.YELLOW + "Encrypting with all shifts:")
        for shift in range(1, 26):
            result = encrypt(args.text, shift)
            print(f"Shift {shift}: {result}")
    else:
        print(Fore.YELLOW + "Decrypting with all shifts:")
        for shift in range(1, 26):
            result = decrypt(args.text, shift)
            print(f"Shift {shift}: {result}")

if __name__ == "__main__":
    main()
