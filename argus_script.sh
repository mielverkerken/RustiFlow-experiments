#!/bin/bash

# Check if the right number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <pcap_file> <output_csv>"
    exit 1
fi

# Input PCAP file
PCAP_FILE="$1"

# Output CSV file
OUTPUT_CSV="$2"

# Run the argus command and pipe its output to ra
argus -r "$PCAP_FILE" -S 3600 -w - | ra -r - -c , -s stime ltime trans flgs dur runtime idle mean stddev sum min max smacclass dmacclass senc denc saddr daddr proto sport dport stos dtos sdsb ddsb sttl dttl shops dhops sipid dipid autoid cause pkts spkts dpkts bytes sbytes dbytes appbytes sappbytes dappbytes pcr load sload dload loss sloss dloss ploss psloss pdloss retrans sretrans dretrans pretrans psretrans pdretrans sgap dgap rate srate drate dir state swin dwin stcpb dtcpb smss dmss tcprtt synack ackdat tcpopt inode offset smeansz dmeansz > "$OUTPUT_CSV"

# Check if the command succeeded
if [ $? -eq 0 ]; then
  echo "Processing completed successfully. Output saved to $OUTPUT_CSV"
else
  echo "An error occurred during processing."
fi
