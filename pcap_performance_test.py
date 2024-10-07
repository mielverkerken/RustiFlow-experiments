import os
import time
import psutil
import subprocess
import csv
import shlex
import threading

# Define the flow exporters
exporters = {
    "rustiflow": {
        "name": "rustiflow", 
        "cmd": "ping -c 5 8.8.8.8"
        # "cmd": "rustiflow -f basic --header --idle-timeout 120 --active-timeout 3600 --output csv --export-path {pcap_file}.csv pcap {pcap_file}.pcap"
    },
    "extractor1": {
        "name": "extractor1", 
        "cmd": "path/to/extractor1"
    }
}

pcap_files = [
    "sample_100k",
    "sample_500k",
    "sample_1M",
    "sample_2M",
    "sample_4M",
    "sample_8M",
]

MONITOR_INTERVAL = 1

# Function to read and discard the output of a process to avoid blocking
def stream_reader(stream):
    for _ in iter(stream.readline, b''):
        pass
    stream.close()

# Save metrics to CSV for later analysis
def save_metrics_to_csv(extractor, pcap, cpu_usage, memory_usage, runtime, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Runtime (s)", "Interval", "CPU_Usage (%)", "Memory_Usage (MB)"])
        
        for i, (cpu, mem) in enumerate(zip(cpu_usage, memory_usage)):
            writer.writerow([runtime, i, cpu, mem])
    # Append row for this experiment to summary CSV

    
# Function to monitor resource usage
def monitor_resources(proc, interval=MONITOR_INTERVAL):
    cpu_usage = []
    memory_usage = []
    
    try:
        # Get process by PID
        process = psutil.Process(proc.pid)
        print(f"Process ID: {process.pid}")

        # Set an initial call to cpu_percent to establish a baseline
        process.cpu_percent(interval=None)
        time.sleep(interval)
        
        # Monitor until process terminates
        while process.is_running() and process.status() != psutil.STATUS_ZOMBIE:
            # Fetch multiple attributes in a single call to optimize performance
            proc_info = process.as_dict(attrs=['cpu_percent', 'memory_info', 'status'], ad_value=None)
            
            # Extract needed metrics
            cpu_usage.append(proc_info['cpu_percent'])
            memory_usage.append(proc_info['memory_info'].rss / (1024 * 1024))  # Memory in MB

            # Sleep for the given interval
            time.sleep(interval)

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    
    return cpu_usage, memory_usage

# Run the flow exporter and capture metrics
def run_exporter(name, pcap_file):
    exporter_command = shlex.split(exporters[name]['cmd'].format(pcap_file=pcap_file))
    print(f"Executing CMD: {exporter_command}")

    start_time = time.time()
    
    # Start the flow exporter process
    with subprocess.Popen(exporter_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
        # Monitor resource usage until process terminates
        cpu_usage, memory_usage = monitor_resources(proc)
        
        # Wait for process completion to avoid zombie state and stop the process
        _, _ = proc.communicate()
        
    end_time = time.time()
    runtime = end_time - start_time
    
    return cpu_usage, memory_usage, runtime

# Main function
if __name__ == "__main__":
    print("Starting pcap performance test with following stats:")
    print(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Logical Cores: {psutil.cpu_count(logical=True)}")
    print(f"Total Memory: {psutil.virtual_memory().total / (1024 * 1024 * 1024)} GB")
    print(f"Available Memory: {psutil.virtual_memory().available / (1024 * 1024 * 1024)} GB")

    exporter_name = "rustiflow"
    for pcap_file in pcap_files:
        print(f"\nRunning flow exporter on {pcap_file}...")
        cpu_usage, memory_usage, runtime = run_exporter(exporter_name, f"monday/{pcap_file}")
        print(f"Finished after {runtime}s")
        
        save_metrics_to_csv(exporter_name, pcap_file, cpu_usage, memory_usage, runtime, f"{exporter_name}_{pcap_file}_metrics.csv")