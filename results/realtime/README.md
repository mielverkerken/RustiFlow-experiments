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
