# caesar_cipher.py
# made by katsuraa 

import argparse
from tqdm import tqdm
import time

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
    # ANSI escape sequences for colors
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"

    ascii_art = f"""
{YELLOW} ░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
 ░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
 ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀    
  █▓▒▒░░░̷B̷̷y̷ ̷K̷̷a̷̷t̷̷s̷̷u̷̷r̷̷a̷̷a̷ ░░░▒▒▓█
    {RESET}"""
    print(ascii_art)
    print(BLUE + "Welcome to Caesar Cipher Tools" + RESET)

    mode = input("Choose mode (encode/decode): ").strip().lower()
    text = input("Enter the text: ").strip()

    if mode not in ["encode", "decode"]:
        print(RED + "Invalid mode selected. Please choose 'encode' or 'decode'." + RESET)
        return

    if mode == "encode":
        print(GREEN + "Encoding with all shifts:" + RESET)
        for shift in range(1, 26):
            with tqdm(total=1, desc=GREEN + f"Shift {shift}" + RESET, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {elapsed}", leave=False) as pbar:
                result = encode(text, shift)
                time.sleep(0.1)  # Simulate work being done
                pbar.update(1)
            print(f"Shift {shift}: {result}")
    else:
        print(YELLOW + "Decoding with all shifts:" + RESET)
        for shift in range(1, 26):
            with tqdm(total=1, desc=GREEN + f"Shift {shift}" + RESET, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} {elapsed}", leave=False) as pbar:
                result = decode(text, shift)
                time.sleep(0.1)  # Simulate work being done
                pbar.update(1)
            print(f"Shift {shift}: {result}")

if __name__ == "__main__":
    main()
