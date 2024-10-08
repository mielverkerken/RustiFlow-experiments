#!/bin/bash

# Check if sufficient arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <exporter> <x>"
    exit 1
fi

# Assign arguments to variables
exporter=$1
repeat_count=$2
pcap_file="cicids2017"
data_dir="/data/cicids2017"
results_dir="results/pcap/$exporter/$pcap_file"

# Create the results directory if it doesn't exist
mkdir -p "$results_dir"

# Loop to repeat the test `x` times
for ((i=1; i<=repeat_count; i++))
do
    echo "Running test $i with exporter $exporter..."

    # Run the Python script for the PCAP test
    python3 pcap_performance_test.py "$exporter" "$data_dir" --pcap "$pcap_file"
    
    # Copy the metrics file to the desired location with incremented name
    cp "$data_dir/${exporter}_${pcap_file}_metrics.csv" "$results_dir/${i}_${exporter}_${pcap_file}_metrics.csv"

    echo "Test $i complete. Metrics copied to $results_dir/${i}_${exporter}_${pcap_file}_metrics.csv"
done

echo "All tests completed successfully."
