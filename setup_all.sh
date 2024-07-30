#!/bin/sh

# Define the script name and path
SCRIPT_NAME="jalankan"
SCRIPT_PATH="$(dirname "$0")/$SCRIPT_NAME"

# Determine target directory based on the environment
if [ -n "$TERMUX_VERSION" ]; then
    TARGET_DIR="/data/data/com.termux/files/usr/bin"
else
    TARGET_DIR="/usr/local/bin"
fi

# Show error message and quit
die(){
    if [ "$*" ]; then
        echo "$*"
    fi
    exit 1
}

# Check if the script already exists in the target directory
if [ -f "$TARGET_DIR/$SCRIPT_NAME" ]; then
    echo "$SCRIPT_NAME already exists in $TARGET_DIR"
    exit 1
fi

# Check if the script exists in the current directory
if [ ! -f "$SCRIPT_PATH" ]; then
    die "$SCRIPT_NAME not found in $(dirname "$0")"
fi

# Move the script to the target directory
sudo mv "$SCRIPT_PATH" "$TARGET_DIR/"
echo "$SCRIPT_NAME moved to $TARGET_DIR"
