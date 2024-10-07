import os
import time
import psutil
import subprocess
import csv
import shlex

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

class Experiment:
    def __init__(self, extractor, folder, pcap):
        self.extractor = extractor
        self.folder = folder
        self.pcap = pcap
        self.cpu = psutil.cpu_count(logical=False)
        self.cpu_logical = psutil.cpu_count(logical=True)
        self.memory = psutil.virtual_memory().total / (1024 * 1024)  # MB
        self.memory_available = psutil.virtual_memory().available / (1024 * 1024)  # MB
        self.cpu_usage = []
        self.memory_usage = []
        self.runtime = 0
        self.datetime = time.strftime('%Y-%m-%d %H:%M:%S')

    def run(self):
        exporter_command = shlex.split(exporters[self.extractor]['cmd'].format(pcap_file=os.path.join(self.folder, self.pcap)))
        print(f"Executing CMD: {exporter_command}")

        start_time = time.time()

        # Start the flow exporter process
        with subprocess.Popen(exporter_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            # Monitor resource usage until process terminates
            self.cpu_usage, self.memory_usage = self.monitor_resources(proc)

            # Wait for process completion to avoid zombie state and stop the process
            proc.communicate()

        end_time = time.time()
        self.runtime = end_time - start_time
        print(f"Finished after {self.runtime}s")

    def monitor_resources(self, proc, interval=MONITOR_INTERVAL):
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
                proc_info = process.as_dict(attrs=['cpu_percent', 'memory_info'], ad_value=None)

                # Extract needed metrics
                cpu_usage.append(proc_info['cpu_percent'])
                memory_usage.append(proc_info['memory_info'].rss / (1024 * 1024))  # Memory in MB

                # Sleep for the given interval
                time.sleep(interval)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

        return cpu_usage, memory_usage

    def save_to_csv(self):
        # Save detailed metrics to a per-run CSV file
        filename = f"{self.extractor}_{self.pcap}_metrics.csv"
        with open(os.path.join(self.folder, filename), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Interval", "CPU_Usage (%)", "Memory_Usage (MB)"])

            for i, (cpu, mem) in enumerate(zip(self.cpu_usage, self.memory_usage)):
                writer.writerow([i, cpu, mem])

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
                summary_writer.writerow(["DateTime", "Extractor", "Folder", "PCAP File", "Runtime (s)", "Avg_CPU_Usage (%)", "Avg_Memory_Usage (MB)", "Max_Memory_Usage (MB)", "CPU Cores", "CPU Logical Cores", "Total Memory (MB)", "Available Memory (MB)"])

            # Write the summary data
            summary_writer.writerow([self.datetime, self.extractor, self.folder, self.pcap, self.runtime, avg_cpu_usage, avg_memory_usage, max_memory_usage, self.cpu, self.cpu_logical, self.memory, self.memory_available])

# Main function
if __name__ == "__main__":
    print("Starting pcap performance test with following stats:")
    print(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    print(f"CPU Logical Cores: {psutil.cpu_count(logical=True)}")
    print(f"Total Memory: {psutil.virtual_memory().total / (1024 * 1024 * 1024)} GB")
    print(f"Available Memory: {psutil.virtual_memory().available / (1024 * 1024 * 1024)} GB")

    exporter_name = "rustiflow"
    folder = "monday"
    for pcap_file in pcap_files:
        print(f"\nRunning flow exporter on {pcap_file}...")
        experiment = Experiment(exporter_name, folder, pcap_file)
        experiment.run()
        experiment.save_to_csv()
