from nfstream import NFStreamer
import argparse
import os


# Function to process offline mode (PCAP file)
def process_offline(pcap_file, output_folder):
    print(f"NFStream processing offline PCAP file: {pcap_file}")

    # Output CSV file based on the PCAP file name
    output_csv = f"nfstream_{os.path.basename(pcap_file)}.csv"

    # NFStreamer for offline PCAP processing
    my_streamer = NFStreamer(
        source=pcap_file,
        idle_timeout=120,
        active_timeout=3600,  # changed default to same as rustiflow
        n_dissections=0,
        statistical_analysis=True,
    )

    # Write the flow results to CSV
    my_streamer.to_csv(os.path.join(output_folder, output_csv))


# Function to process real-time mode (Network Interface)
def process_realtime(interface, output_folder):
    print(f"NFStream processing in real-time on interface: {interface}")

    # NFStreamer for real-time traffic capture
    my_streamer = NFStreamer(
        source=interface,
        idle_timeout=120,
        active_timeout=3600,  # changed default to same as rustiflow
        n_dissections=0,
        statistical_analysis=True,
        performance_report=5,
    )

    # Output CSV file based on the PCAP file name
    output_csv = f"nfstream_{os.path.basename(interface)}.csv"

    # Write the flow results to CSV
    my_streamer.to_csv(os.path.join(output_folder, output_csv))


# Main function
if __name__ == "__main__":
    # Parsing command-line arguments
    parser = argparse.ArgumentParser(
        description="Run NFStreamer in offline (PCAP) or real-time (interface) mode."
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--offline", type=str, help="Path to the PCAP file for offline processing."
    )
    mode_group.add_argument(
        "--realtime",
        type=str,
        help="Network interface for real-time traffic processing.",
    )

    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="The output folder for the CSV file with the flow results.",
    )

    args = parser.parse_args()

    # Offline mode: process the PCAP file
    if args.offline:
        process_offline(args.offline, args.output)

    # Real-time mode: process the network interface
    elif args.realtime:
        process_realtime(args.realtime, args.output)
