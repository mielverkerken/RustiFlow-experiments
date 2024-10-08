#!/bin/bash

# Check if the exporter was passed as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <exporter>"
    exit 1
fi

# Assign the first argument as the exporter
exporter=$1

# Array containing the days of the week
days=("monday" "tuesday" "wednesday" "thursday" "friday" "cicids2017")

# Base source folder path where the Python script outputs files
base_source="/data"

#Destination folder path where files will be copied
destination_folder="results/stats-pcaps"

# Loop through each day in the array
for day in "${days[@]}"; do
    # Source folder for the current day
    source_folder="${base_source}/${day}"

    # Create the destination folder if it doesn't exist
    mkdir -p "$destination_folder"

    # Copy all CSV files matching the extractor's output for the current day
    echo "Copying files from ${source_folder} to ${destination_folder}..."

    # Find and copy the relevant files (e.g., rustiflow_sample_100k.csv)
    find "$source_folder" -name "*_stat.csv" -exec cp {} "$destination_folder" \;

    # Check if the copy was successful
    if [ $? -eq 0 ]; then
        echo "Files for ${day} copied successfully."
    else
        echo "Failed to copy files for ${day}."
    fi

    echo "---------------------------------------------"
done
