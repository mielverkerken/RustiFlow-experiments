import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import FuncFormatter

# Function to parse iftop log file
def parse_iftop_log(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    # Regular expressions to match the total send and receive rates
    send_pattern = re.compile(r'Total send rate:\s+([0-9.]+[KMGb]+)\s+([0-9.]+[KMGb]+)\s+([0-9.]+[KMGb]+)')
    receive_pattern = re.compile(r'Total receive rate:\s+([0-9.]+[KMGb]+)\s+([0-9.]+[KMGb]+)\s+([0-9.]+[KMGb]+)')
    time_pattern = re.compile(r'Listening on')

    timestamps = []
    send_rates = []
    receive_rates = []

    current_time = 0
    for line in lines:
        if time_pattern.search(line):
            current_time += 10
        send_match = send_pattern.search(line)
        if send_match:
            send_rate = send_match.group(2)
            send_rates.append(convert_to_bps(send_rate))
            timestamps.append(current_time)

        receive_match = receive_pattern.search(line)
        if receive_match:
            receive_rate = receive_match.group(2)
            receive_rates.append(convert_to_bps(receive_rate))

    return timestamps, send_rates, receive_rates

# Function to convert traffic rates to bits per second
def convert_to_bps(rate):
    match = re.match(r"([0-9.]+)([a-zA-Z]+)", rate)
    if not match:
        raise ValueError(f"Invalid rate format: {rate}")
    
    value, unit = match.groups()
    value = float(value)
    
    if unit == 'b':
        return value
    elif unit == 'Kb':
        return value * 1e3
    elif unit == 'Mb':
        return value * 1e6
    elif unit == 'Gb':
        return value * 1e9
    elif unit == 'Tb':
        return value * 1e12
    else:
        raise ValueError(f"Unrecognized unit: {unit}")
    
# Formatter function to convert seconds to hh:mm:ss format
def seconds_to_hhmmss(x, pos):
    hrs, rem = divmod(x, 3600)
    mins, secs = divmod(rem, 60)
    return f'{int(hrs):02}:{int(mins):02}:{int(secs):02}'

# Parse the log file
LOG_FILE = "iftop_data.log"
timestamps, send_rates, receive_rates = parse_iftop_log(LOG_FILE)

# Create a DataFrame
df = pd.DataFrame({
    'Time': timestamps,
    'Send Rate (bps)': send_rates,
    'Receive Rate (bps)': receive_rates
})

# Plot the data
plt.figure(figsize=(10, 5))
# plt.plot(df['Time'], df['Send Rate (bps)'], label='Send Rate')
plt.plot(df['Time'], df['Receive Rate (bps)']/1e6, '.-', label='Receive Rate')
plt.xlabel('Time')
plt.ylabel('Mbps')
plt.title('Throughput Over Time')
# plt.legend()


# Set x-axis formatter to display time in hh:mm:ss
formatter = FuncFormatter(seconds_to_hhmmss)
plt.gca().xaxis.set_major_formatter(formatter)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('iftop_data.png')

avg_receive_rates = sum(receive_rates)/len(receive_rates)
print(f"Average Receive Rate: {avg_receive_rates/1e6:.2f} Mbps")
