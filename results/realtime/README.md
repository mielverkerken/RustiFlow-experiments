# Realtime Results

- `sudo apt install tcpreplay`
- `iperf3 -c ipaddress -t time -b throughputG`
- `tcpreplay -i interface -t file.pcap`

```sh
sudo tcprewrite --mtu=1500 --mtu-trunc --infile=<filename>.pcap
--outfile=<new filename>.pcap --srcipmap=0.0.0.0/0:<IP address>
--dstipmap=0.0.0.0/0:<IP address>

# For monday
sudo tcprewrite --mtu=1500 --mtu-trunc --infile=/data/monday/monday.pcap --outfile=/data/monday/monday-trunc.pcap
--srcipmap=0.0.0.0/0:192.168.0.2 --dstipmap=0.0.0.0/0:192.168.0.1
```

## Experiments

- Iperf (stability test, TCP vs UDP)
  - Max throughput localhost
  - increment throughput in steps (10mbit, 100mbit, 1Gbit, 10Gbit, 100Gbit)
  - measure throughput, cpu, mem and retries (lost packets)
- Tcpreplay (simulating real network traffic, variablity)
  - Max throughput localhost
  - increment throughput in steps (10mbit, 100mbit, 1Gbit, 10Gbit, 100Gbit)
  - measure throughput, cpu, mem and retries (lost packets)
- Case study: Datacenter uplink (24h or whole week) (only Rustiflow)

## IPerf3 results

- Server: `iperf3 -s -i 1 --json --logfile iperf_server_{exporter}.json`
- Client: `python3 ./realtime_performance_test.py <exporter>`
  This will run Iperf3 client with increasing bitrates (1M, 10M, 100M, 1G, 10G) in bidirectional mode for 5 minutes while monitoring the flow exporter.
