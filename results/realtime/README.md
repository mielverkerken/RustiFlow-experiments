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

```sh
sudo tcprewrite --mtu=1500 --mtu-trunc --infile=/data/cicids2017/cicids2017.pcap --outfile=/data/cicids2017/cicids2017-trunc.pcap --enet-dmac=00:25:90:dc:43:d2 --enet-smac=0c:c4:7a:0b:9f:76
sudo tcpreplay -i eno3 --duration=300 --mbps=8 /data/cicids2017/cicids2017-trunc.pcap
```

## Experiments ideas

- Iperf (stability test, TCP vs UDP)
  - Max throughput localhost
  - increment throughput in steps (10mbit, 100mbit, 1Gbit, 10Gbit, 100Gbit)
  - measure throughput, cpu, mem and retries (lost packets)
- Tcpreplay (simulating real network traffic, variablity)
  - Max throughput localhost
  - increment throughput in steps (10mbit, 100mbit, 1Gbit, 10Gbit, 100Gbit)
  - measure throughput, cpu, mem and retries (lost packets)
- Case study: Datacenter uplink (24h or whole week) (only Rustiflow)

# Experiments Setup

## IPerf3 Localhost

Run from node0 (192.168.0.1) on localhost

```sh
iperf3_run.sh <exporter> <interface> [duration] [serverip]

iperf3_run.sh rustiflow lo 300 127.0.0.1
```
