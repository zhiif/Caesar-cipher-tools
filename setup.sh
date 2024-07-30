#!/bin/bash

# Define the script name and path
SCRIPT_NAME="jalankan.sh"
SCRIPT_PATH="$(dirname "$0")/$SCRIPT_NAME"

# Define the target directory
TARGET_DIR="/usr/local/bin"

# The name of the program after installation:
PROGRAM="jalankan";

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

# Move the script to the target directory
if [ -f "$SCRIPT_PATH" ]; then
    sudo mv "$SCRIPT_PATH" "$TARGET_DIR/"
    echo "$SCRIPT_NAME moved to $TARGET_DIR"
else
    die "$SCRIPT_NAME not found"
fi
