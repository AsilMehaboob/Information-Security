#!/bin/bash

echo "Enter the filename:"
read filename

if [ -f "$filename" ]
then
    chmod -x "$filename"
    echo "Execution permission removed from $filename"
else
    echo "File $filename does not exist."
fi