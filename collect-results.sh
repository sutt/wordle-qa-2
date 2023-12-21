#!/bin/bash

# Directory where files will be moved
destination_dir="results"

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Move files matching 'output*' pattern
find . -type f -name "output*" -exec mv {} "$destination_dir" \;

# Move files matching 'grade*' pattern
find . -type f -name "grade*" -exec mv {} "$destination_dir" \;
