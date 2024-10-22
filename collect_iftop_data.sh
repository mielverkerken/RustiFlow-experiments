#!/bin/bash
# Collect iftop data every X seconds and save to a file
INTERVAL=10
OUTPUT_FILE="iftop_data.log"

# Function to handle cleanup
cleanup() {
    echo "Stopping data collection..."
    exit 0
}

# Trap SIGINT (Ctrl+C) and call the cleanup function
trap cleanup SIGINT

echo -n "Collecting iftop data"
while true; do
    sudo iftop -t -s $INTERVAL -L 10 -n -p -i eno3 >> $OUTPUT_FILE 2>/dev/null
    echo -n "."
    sleep $INTERVAL
done
