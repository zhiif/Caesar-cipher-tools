# caesar_cipher.py
# made by katsuraa 

import argparse
from colorama import Fore, Style, init

def encode(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decode(text, shift):
    return encode(text, -shift)

def main():
    init(autoreset=True)
    ascii_art = f"""
{Fore.YELLOW} ░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
 ░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
 ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀    
  █▓▒▒░░░̷B̷̷y̷ ̷K̷̷a̷̷t̷̷s̷̷u̷̷r̷̷a̷̷a̷ ░░░▒▒▓█
    """
    print(ascii_art)
    print(Fore.BLUE + "Welcome to Caesar Cipher Tool" + Style.DIM)

    parser = argparse.ArgumentParser(description="Caesar Cipher Tool")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose whether to encode or decode the text")
    parser.add_argument("text", help="The text to encode or decode")
    args = parser.parse_args()

    if args.mode == "encode":
        print(Fore.GREEN + "Encoding with all shifts:")
        for shift in range(1, 26):
            result = encode(args.text, shift)
            print(f"Shift {shift}: {result}")
    else:
        print(Fore.YELLOW + "Decoding with all shifts:")
        for shift in range(1, 26):
            result = decode(args.text, shift)
            print(f"Shift {shift}: {result}")

if __name__ == "__main__":
    main()
