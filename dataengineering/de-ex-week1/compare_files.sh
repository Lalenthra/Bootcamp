#!/bin/bash

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <file1.csv> <file2.csv>"
    exit 2  # Exit with code 2 for incorrect usage
fi

file1="$1"
file2="$2"

# Check if both files exist
if [ ! -f "$file1" ]; then
    echo "Error: File $file1 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

if [ ! -f "$file2" ]; then
    echo "Error: File $file2 does not exist."
    exit 2  # Exit with code 2 for file not found
fi

# Compare the files
if cmp -s "$file1" "$file2"; then
    echo "The CSV files are identical."
    exit 0  # Exit with code 0 if files are the same
else
    echo "The CSV files are different."

    # Optional: Show the differences
    echo "Differences:"
    diff "$file1" "$file2"

    exit 1  # Exit with code 1 if files are different
fi
