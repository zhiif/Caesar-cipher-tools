#!/usr/bin/env python3
# caesar_cipher.py
# made by katsuraa 
# smileyoursystem

import time
import itertools
import sys

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

def display_loading_bar(duration=0.5, length=40):
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    for i in range(length):
        time.sleep(duration / length)
        sys.stdout.write('\033[92m\r')  # Mengatur warna hijau
        sys.stdout.write(f"Memproses... [{'█' * (i + 1)}{' ' * (length - i - 1)}] {int((i + 1) / length * 100)}% {next(spinner)}")
        sys.stdout.flush()
    sys.stdout.write('\r' + ' ' * (length + 40) + '\r')  # Menghapus loading bar setelah selesai

def main():
    # ANSI escape sequences for colors
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"

    ascii_art = f"""
{YELLOW} ╔───────────────────────────────────────────────────────╗
 │░░░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄░░░│
 │░░░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄░░░│
 │░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀░░░│
 ╚───🖳 █▓▒▒░░̷ B̷̷y̷ ̷K̷̷a̷̷t̷̷s̷̷u̷̷r̷̷a̷̷a̷ ░░▒▒▓█ 🖳───╝   
 
    {RESET}"""
    print(ascii_art)
    print(BLUE + "Welcome to Caesar Cipher Tools" + RESET)

    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter the text: ").strip()

    if mode not in ["encrypt", "decrypt"]:
        print(RED + "Invalid mode selected. Please choose 'encrypt' or 'decrypt'." + RESET)
        return

    if mode == "encrypt":
        print(GREEN + "encryption with all shifts:" + RESET)
        for shift in range(1, 26):
            print(f"\nShift {shift}: ", end='', flush=True)
            display_loading_bar()
            result = encrypt(text, shift)
            print(f"Shift {shift}: {result}")
    else:
        print(YELLOW + "decryption with all shifts:" + RESET)
        for shift in range(1, 26):
            print(f"\nShift {shift}: ", end='', flush=True)
            display_loading_bar()
            result = decrypt(text, shift)
            print(f"Shift {shift}: {result}")

if __name__ == "__main__":
    main()
