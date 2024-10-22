#!/bin/bash
# Collect iftop data every X seconds and save to a file
INTERVAL=10
OUTPUT_FILE="iftop_data.log"

# Check if an interface was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <network_interface>"
    exit 1
fi

INTERFACE=$1

# Function to handle cleanup
cleanup() {
    echo "Stopping data collection..."
    exit 0
}

# Trap SIGINT (Ctrl+C) and call the cleanup function
trap cleanup SIGINT

echo -n "Collecting iftop data on interface $INTERFACE"
while true; do
    sudo iftop -t -s $INTERVAL -L 10 -n -p -i "$INTERFACE" >> $OUTPUT_FILE 2>/dev/null
    echo -n "."
    sleep $INTERVAL
done
