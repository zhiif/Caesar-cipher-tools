# caesar_cipher.py
# made by katsuraa 

import argparse
from colorama import Fore, Style, init, AnsiToWin32
from tqdm import tqdm
import time
import sys

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
    init(autoreset=True, strip=False)
    if sys.stdout.isatty():
        sys.stdout = AnsiToWin32(sys.stdout).stream

    ascii_art = f"""
{Fore.YELLOW} ░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
 ░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
 ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀    
  █▓▒▒░░░̷B̷̷y̷ ̷K̷̷a̷̷t̷̷s̷̷u̷̷r̷̷a̷̷a̷ ░░░▒▒▓█
    """
    print(ascii_art)
    print("\033[94m" + "Welcome to Caesar Cipher Tools" + "\033[0m")

    mode = input("Choose mode (encode/decode): ").strip().lower()
    text = input("Enter the text: ").strip()

    if mode not in ["encode", "decode"]:
        print(Fore.RED + "Invalid mode selected. Please choose 'encode' or 'decode'.")
        return

    if mode == "encode":
        print(Fore.GREEN + "Encoding with all shifts:")
        for shift in range(1, 26):
            with tqdm(total=1, desc=Fore.GREEN + f"Shift {shift}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {elapsed}", leave=False) as pbar:
                result = encode(text, shift)
                time.sleep(0.1)  # Simulate work being done
                pbar.update(1)
            print(f"Shift {shift}: {result}")
    else:
        print(Fore.YELLOW + "Decoding with all shifts:")
        for shift in range(1, 26):
            with tqdm(total=1, desc=Fore.GREEN + f"Shift {shift}", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {elapsed}", leave=False) as pbar:
                result = decode(text, shift)
                time.sleep(0.1)  # Simulate work being done
                pbar.update(1)
            print(f"Shift {shift}: {result}")

if __name__ == "__main__":
    main()
