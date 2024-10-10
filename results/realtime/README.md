# Realtime Results

- `iperf3 -c ipaddress -t time -b throughputG`
- `tcpreplay -i interface -t file.pcap`
- 
    ```sh
    sudo tcprewrite --mtu=1500 --mtu-trunc --infile=<filename>.pcap
    --outfile=<new filename>.pcap --srcipmap=0.0.0.0/0:<IP address>
    --dstipmap=0.0.0.0/0:<IP address>
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