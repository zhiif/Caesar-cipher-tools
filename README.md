# Caesar Cipher Tools
This caesar cipher can be used on linux, termux and windows.

## Table of contents
- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Linux/termux](#linuxtermux)
  - [Windows](#windows)
- [Use](#use)
- [Contoh](#contoh)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

### Description
This program encode and decode the Caesar cipher.

### Requirements
- git
- This tool run on `Python3`. Install it if you don't have it.
- Root privilege (for `Linux` users)
##### Installation Python3
```bash
#linux/termux
apt install python3
#windows
kunjungi situs resmi python untuk penginstalan
```
download[python](https://www.python.org/downloads/windows/) for windows

### Installation
#### Linux/termux
```bash
# Clone repository
git clone https://github.com/zhiif/caesar-cipher-tools

# Go to the directory.
cd caesar-cipher-tools

# See directory contents.
ls
```
Important: If you are using ```Linux```, you must log in as the `root user`.
#### Windows
```bash
# Clone repository
git clone https://github.com/zhiif/caesar-cipher-tools

# Go to the directory.
cd caesar-cipher-tools

# See directory contents.
dir
```

### Use
How to run
```bash
# encoding into a Caesar cipher.
python3 caesar.py encode "Hello, World"
# decoding Caesar cipher
python3 caesar.py decode "Rovvy, Gybvn"
```
* Replace ```"Hello, World"``` with your word.
* Replace ```"Rovvy, Gybvn"``` with the caesar cipher you want to decode.
