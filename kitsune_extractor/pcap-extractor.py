import argparse
import numpy as np
import csv
from FeatureExtractor import FE

def extract_features(pcap_file, output_file, packet_limit=np.inf):
    # Initialize the feature extractor
    extractor = FE(pcap_file, packet_limit)
    
    # Open the output CSV file and write the feature vectors
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        while True:
            features = extractor.get_next_vector()
            if features is None or len(features.size) == 0:
                break
            writer.writerow(features)
    
    print(f"Feature extraction complete. Output written to {output_file}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract network flow features from a pcap file.")
    parser.add_argument("pcap_file", type=str, help="Path to the pcap file.")
    parser.add_argument("output_file", type=str, help="Path to the output CSV file.")
    parser.add_argument("--limit", type=int, default=np.inf, help="Limit the number of packets to process.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the feature extraction function with the provided arguments
    extract_features(args.pcap_file, args.output_file, args.limit)

if __name__ == "__main__":
    main()