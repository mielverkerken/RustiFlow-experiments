#!/bin/bash

# Array containing the days of the week
days=("monday" "tuesday" "wednesday" "thursday" "friday")

# Path to your Python script
python_script="pcap_performance_test.py"

# Exporter to use
exporter="rustiflow"

# Base folder path
base_folder="/data"

# Loop through each day in the array
for day in "${days[@]}"; do
    # Construct the folder path for the current day
    folder="${base_folder}/${day}"

    # Print the command being executed
    echo "Running test for ${day} in folder ${folder}..."

    # Call the Python script with the exporter and folder
    python3 "$python_script" "$exporter" "$folder"

    # Check if the script executed successfully
    if [ $? -eq 0 ]; then
        echo "Test for ${day} completed successfully."
    else
        echo "Test for ${day} failed."
    fi

    echo "---------------------------------------------"
done
