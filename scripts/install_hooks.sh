#!/bin/bash

# Define the source and target paths
HOOK_NAME="post-merge"
SOURCE_HOOK_PATH=".githooks/${HOOK_NAME}"
TARGET_HOOK_PATH=".git/hooks/${HOOK_NAME}"

echo "--- Installing Git Hooks ---"

# Check if the target hook already exists
if [ -f "${TARGET_HOOK_PATH}" ]; then
    if [ -L "${TARGET_HOOK_PATH}" ]; then
        echo "Existing symbolic link found. Skipping installation."
        exit 0
    fi
    echo "Existing hook file found. Backing up to ${TARGET_HOOK_PATH}.bak"
    mv "${TARGET_HOOK_PATH}" "${TARGET_HOOK_PATH}.bak"
fi

# Create a symbolic link from the committed file to the Git hooks directory
# Using 'ln -s' (symbolic link) ensures changes to the committed file are reflected immediately.
ln -s "../${SOURCE_HOOK_PATH}" "${TARGET_HOOK_PATH}"

# Ensure the committed script is executable
chmod +x "${SOURCE_HOOK_PATH}"

echo "Git hook '${HOOK_NAME}' successfully installed and linked."
echo "It will run automatically after every 'git pull' or 'git merge'."
