import os
import time
import psutil
import subprocess
import csv
import shlex
import argparse
import threading
import json

# Define the flow exporters
exporters = {
    "rustiflow": {
        "name": "rustiflow", 
        "shell": False,
        "cmd": "sudo ./rustiflow -f cic --header --idle-timeout 120 --active-timeout 3600 --output csv --export-path {output_folder}/rustiflow_realtime.csv realtime {interface}",
        "cwd": "/users/mverkerk/RustiFlow/target/release/",
    },
    "cicflowmeter": {
        "name": "cicflowmeter", 
        "shell": False,
        "cmd": "./cfm {pcap_file}.pcap {output_folder}",
        "cwd": "/users/mverkerk/CICFlowMeter/build/distributions/CICFlowMeter-4.0/bin", # Issues with libraries is running from other directory
    },
    "nfstream": {
        "name": "nfstream", 
        "shell": False,
        "cmd": "python3 /users/mverkerk/RustiFlow-experiments/nfstream_script.py --offline {pcap_file}.pcap --output {output_folder}",
        "cwd": None, # Runs from any directory
    },
    "argus": {
        "name": "argus",
        "shell": True,
        "cmd": "/users/mverkerk/RustiFlow-experiments/argus_script.sh {pcap_file}.pcap {pcap_file}_argus.csv",
        "cwd": None, # Runs from any directory
    },
    "go-flows": {
        "name": "go-flows",
        "shell": False,
        "cmd": "/users/mverkerk/go-flows/go-flows run features /users/mverkerk/RustiFlow-experiments/go-flows-features.json export csv {pcap_file}_go-flows.csv source libpcap {pcap_file}.pcap",
        "cwd": None, # Runs from any directory
    },
    "zeek": {
        "name": "zeek",
        "shell": False,
        "cmd": "/opt/zeek/bin/zeek -r {pcap_file}.pcap",
        "cwd": "{output_folder}", # Write all output here
    },
    "ntlflowlyzer": {
        "name": "ntlflowlyzer",
        "shell": False,
        "cmd": "ntlflowlyzer -c /users/mverkerk/RustiFlow-experiments/ntlflowlyzer_config.json",
        "cwd": None, # Runs from any directory
    },
    "nprobe": {
        "name": "nprobe",
        "shell": False,
        "cmd": "nprobe -i {pcap_file}.pcap -n none -t 3600 -d 120 --csv-separator , -P {output_folder} -V 9  -T '%IPV4_SRC_ADDR %IPV4_DST_ADDR %L4_SRC_PORT %L4_DST_PORT %PROTOCOL %L7_PROTO %IN_BYTES %OUT_BYTES %IN_PKTS %OUT_PKTS %FLOW_DURATION_MILLISECONDS %TCP_FLAGS %CLIENT_TCP_FLAGS %SERVER_TCP_FLAGS %DURATION_IN %DURATION_OUT %MIN_TTL %MAX_TTL %LONGEST_FLOW_PKT %SHORTEST_FLOW_PKT %MIN_IP_PKT_LEN %MAX_IP_PKT_LEN %SRC_TO_DST_SECOND_BYTES %DST_TO_SRC_SECOND_BYTES %RETRANSMITTED_IN_BYTES %RETRANSMITTED_IN_PKTS %RETRANSMITTED_OUT_BYTES %RETRANSMITTED_OUT_PKTS %SRC_TO_DST_AVG_THROUGHPUT %DST_TO_SRC_AVG_THROUGHPUT %NUM_PKTS_UP_TO_128_BYTES %NUM_PKTS_128_TO_256_BYTES %NUM_PKTS_256_TO_512_BYTES %NUM_PKTS_512_TO_1024_BYTES %NUM_PKTS_1024_TO_1514_BYTES %TCP_WIN_MAX_IN %TCP_WIN_MAX_OUT %ICMP_TYPE %ICMP_IPV4_TYPE %DNS_QUERY_ID %DNS_QUERY_TYPE %DNS_TTL_ANSWER %FTP_COMMAND_RET_CODE'",
        "cwd": None, # Runs from any directory
    },
    "kitsune": {
        "name": "kitsune",
        "shell": False,
        "cmd": "python3 pcap-extractor.py {pcap_file}.pcap {pcap_file}_kitsune.csv",
        "cwd": "/users/mverkerk/RustiFlow-experiments/kitsune_extractor",
    },
    "joy": {
        "name": "joy",
        "shell": False,
        "cmd": "joy bidir=1 output=joy.json.gz {pcap_file}.pcap",
        "cwd": "{output_folder}",
    },
}

MONITOR_INTERVAL = 1  # Interval in seconds for resource monitoring

class Experiment:
    def __init__(self, extractor, folder, interface):
        self.extractor = extractor
        self.folder = folder
        self.interface = interface
        self.cpu = psutil.cpu_count(logical=False)
        self.cpu_logical = psutil.cpu_count(logical=True)
        self.memory = psutil.virtual_memory().total / (1024 * 1024)  # MB
        self.memory_available = psutil.virtual_memory().available / (1024 * 1024)  # MB
        self.cpu_usage = []
        self.memory_usage = []
        self.cpu_num = []
        self.num_threads = []
        self.open_files = []
        self.num_ctx_switches = []
        self.num_children = []
        self.runtime = 0
        self.datetime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.stop_event = threading.Event()
        self._terminate = False

    def run(self):
        exporter_command = exporters[self.extractor]['cmd'].format(interface=self.interface, output_folder=self.folder)
        cwd = exporters[self.extractor]['cwd']
        shell = exporters[self.extractor]['shell']

        if not shell:
            exporter_command = shlex.split(exporter_command)

        if self.extractor in ["zeek", "joy"]:
            cwd = cwd.format(output_folder=self.folder)

        if self.extractor == "ntlflowlyzer":
            with open("/users/mverkerk/RustiFlow-experiments/ntlflowlyzer_config.json", "r") as file:
                config = json.load(file)
                config['pcap_file_address'] = os.path.join(self.folder, f"{self.pcap}.pcap")
                config['output_file_address'] = os.path.join(self.folder, f"{self.pcap}_ntlflowlyzer.csv")

            with open("/users/mverkerk/RustiFlow-experiments/ntlflowlyzer_config.json", "w") as file:
                json.dump(config, file, indent=4)

        print(f"Executing CMD: {exporter_command}")

        start_time = time.time()

        try:
            # Start the flow exporter process
            with subprocess.Popen(exporter_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd, shell=shell) as proc:
                # Start the resource monitoring in a separate thread
                monitor_thread = threading.Thread(target=self.monitor_resources, args=(proc,))
                monitor_thread.start()

                # Wait for process completion
                _, stderr = proc.communicate()

                # Print error if it occurred
                if proc.returncode != 0:
                    print(f"Error occurred while running the command:\n{stderr}")

                # Signal the monitoring thread to stop and wait for it to finish
                self.stop_event.set()
                monitor_thread.join()
        except KeyboardInterrupt:
            print("\nProcess interrupted by user (Ctrl+C). Stopping...")
            self.stop_event.set()
            monitor_thread.join()
            self._terminate = True

        end_time = time.time()
        self.runtime = end_time - start_time
        print(f"Finished after {self.runtime}s")

    def monitor_resources(self, proc):
        try:
            # Get the parent process by its PID
            parent_process = psutil.Process(proc.pid)
            print(f"Process ID: {parent_process.pid}")

            # Initialize the process map with the parent process
            process_map = {parent_process.pid: parent_process}

            while not self.stop_event.is_set() and parent_process.is_running():
                # Refresh children processes and update the process map
                children = parent_process.children(recursive=True)

                # Add new children to the process map
                for child in children:
                    if child.pid not in process_map:
                        process_map[child.pid] = child

                
                # Remove child processes that have finished
                children_pids = [child.pid for child in children]
                finished_pids = [pid for pid in process_map if pid not in children_pids and pid != parent_process.pid]
                for pid in finished_pids:
                    del process_map[pid]

                # Aggregate CPU and memory statistics for all processes in the map
                total_cpu_percent = 0.0
                total_memory_usage = 0.0
                total_cpu_num = []
                total_num_threads = 0
                total_open_files = 0
                total_ctx_switches = 0

                for p in process_map.values():
                    try:
                        # Collect resource metrics from each (child) process
                        proc_info = p.as_dict(attrs=['cpu_percent', 'memory_info', 'cpu_num', 'num_threads', 'open_files', 'num_ctx_switches'])
                        
                        total_cpu_percent += proc_info['cpu_percent']
                        total_memory_usage += proc_info['memory_info'].rss / (1024 * 1024)  # Memory in MB
                        total_cpu_num.append(proc_info['cpu_num'])
                        total_num_threads += proc_info['num_threads']
                        total_open_files += len(proc_info['open_files']) if proc_info['open_files'] else 0
                        total_ctx_switches += proc_info['num_ctx_switches'].voluntary + proc_info['num_ctx_switches'].involuntary

                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        # Handle the case where the (child) process ends before stats can be collected
                        continue

                # Append the aggregated resource metrics for this interval
                self.cpu_usage.append(total_cpu_percent)
                self.memory_usage.append(total_memory_usage)
                self.cpu_num.append(total_cpu_num)
                self.num_threads.append(total_num_threads)
                self.open_files.append(total_open_files)
                self.num_ctx_switches.append(total_ctx_switches)
                self.num_children.append(len(children))

                # Wait for the next interval
                self.stop_event.wait(MONITOR_INTERVAL)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


    def save_to_csv(self):
        # Save detailed metrics to a per-run CSV file
        filename = f"{self.extractor}_realtime_{self.interface}_metrics.csv"
        with open(os.path.join(self.folder, filename), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Interval", "CPU_Usage (%)", "Memory_Usage (MB)", "CPU_Num", "Num_Threads", "Open_Files", "Context_Switches", "Child Processes"])

            for i, (cpu, mem, cpu_num, num_threads, open_files, ctx_switches, num_children) in enumerate(zip(self.cpu_usage, self.memory_usage, self.cpu_num, self.num_threads, self.open_files, self.num_ctx_switches, self.num_children)):
                writer.writerow([i+1, cpu, mem, cpu_num, num_threads, open_files, ctx_switches, num_children])

        # Calculate average CPU and memory usage for summary
        avg_cpu_usage = sum(self.cpu_usage) / len(self.cpu_usage) if self.cpu_usage else 0
        avg_memory_usage = sum(self.memory_usage) / len(self.memory_usage) if self.memory_usage else 0
        max_memory_usage = max(self.memory_usage) if self.memory_usage else 0

        # Append row for this experiment to the summary CSV
        summary_filename = "summary_metrics.csv"
        file_exists = os.path.isfile(summary_filename)
        with open(summary_filename, mode='a', newline='') as summary_file:
            summary_writer = csv.writer(summary_file)
            if not file_exists:
                # Write header if file does not exist
                summary_writer.writerow(["DateTime", "Extractor", "Folder", "Interface", "Runtime (s)", "Avg_CPU_Usage (%)", "Avg_Memory_Usage (MB)", "Max_Memory_Usage (MB)", "CPU Cores", "CPU Logical Cores", "Total Memory (MB)", "Available Memory (MB)"])

            # Write the summary data
            summary_writer.writerow([self.datetime, self.extractor, self.folder, self.interface, self.runtime, avg_cpu_usage, avg_memory_usage, max_memory_usage, self.cpu, self.cpu_logical, self.memory, self.memory_available])

# Main function
if __name__ == "__main__":

    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description="Run online performance tests using specified exporter and folder.")
    parser.add_argument("exporter", type=str, help="The name of the flow exporter to use (e.g., rustiflow or extractor1).")
    parser.add_argument("folder", type=str, help="The output folder.")
    parser.add_argument("--interface", type=str, help="The interface to capture packets from.")
    args = parser.parse_args()

    exporter_name = args.exporter
    folder = args.folder

    if exporter_name not in exporters:
        print(f"Error: Exporter '{exporter_name}' is not defined.")
        exit(1)

    if not os.path.isdir(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        exit(1)

    if args.interface == None:
        print("Error: Interface not provided.")
        exit(1)
    
    print("Starting realtime performance test with following stats:")
    print(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Logical Cores: {psutil.cpu_count(logical=True)}")
    print(f"Total Memory: {psutil.virtual_memory().total / (1024 * 1024 * 1024)} GB")
    print(f"Available Memory: {psutil.virtual_memory().available / (1024 * 1024 * 1024)} GB")


    print(f"\nRunning flow exporter on interface {args.interface}...")
    experiment = Experiment(exporter_name, folder, args.interface)
    experiment.run()
    experiment.save_to_csv()
