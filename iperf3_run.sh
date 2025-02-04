#!/bin/bash

# Check if an exporter was passed as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <exporter> <interface>"
    exit 1
fi

# Check if an interface was passed as an argument
if [ -z "$2" ]; then
    echo "Usage: $0 <exporter> <interface>"
    exit 1
fi

# Assign the first argument as the exporter
exporter=$1
interface=$2

# Path to your Python script
python_script="realtime_performance_test.py"

# Base folder path
folder="/users/mverkerk/RustiFlow-experiments/results/realtime/${exporter}"
mkdir -p "$folder"

# Print the command being executed
echo "Running test for ${exporter} with results in ${folder}..."

# Call the Python script with the exporter and folder
python3 "$python_script" "$exporter" "$folder" "--interface" "$interface" "--throughput" "all"

# Check if the script executed successfully
if [ $? -eq 0 ]; then
    echo "Test for ${exporter} completed successfully."
else
    echo "Test for ${exporter} failed."
fi

echo "---------------------------------------------"
