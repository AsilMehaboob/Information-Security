#!/bin/bash

dir="."
count=1

echo "S.No | File Name | Creation Date"
echo "--------------------------------"

for file in "$dir"/*
do 
	if [ -f "$file" ]; then
		creation_date=$(stat -c %w "$file")

		if [ "$creation_date" = "-" ]; then
			creation_date=$(stat -c "%y" "$file" | cut -d ' ' -f1)
		fi
	
	echo "$count | $(basename "$file") | $creation_date"
	count=$((count + 1))
	fi
done