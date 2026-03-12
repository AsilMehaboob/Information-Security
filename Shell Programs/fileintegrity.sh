#!/bin/bash

echo "Enter filename to check integrity:"
read filename

hashfile="hashfile.txt"

if [ ! -f "$hashfile" ]; then
    echo "Creating hash for "$filename""
    sha256sum "$filename" > "$hashfile"
    echo "Hash created and stored in "$hashfile""
else
    echo "Checking integrity of "$filename""

    sha256sum -c "$hashfile"
fi