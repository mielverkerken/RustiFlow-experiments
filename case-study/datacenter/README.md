## Setup

- ifstat: no dns lookup and log network throughput every 5 seconds
- tcpdump: Running to make sure all packets go to rustiflow, write capture (first 64 bytes) to /dev/null
- rustiflow: run script that start rustiflow and monitors cpu and mem usage

```sh
screen -dmS ifstat bash -c "ifstat -i eno3 -n -t 5 > /data/rustiflow/ifstat.log 2>&1"

screen -dmS tcpdump bash -c "sudo tcpdump --immediate-mode --buffer-size=32768 --packet-buffered -n --interface=eno3 -s 64 -w /dev/null > /data/rustiflow/tcpdump.log 2>&1"
screen -dmS rustiflow bash -c "python3 /users/mverkerk/RustiFlow-experiments/realtime_performance_test.py rustiflow /data/rustiflow --interface eno3 > rustiflow.log 2>&1"
```

- Afterwards, kill all screens:

```sh
for session in $(screen -ls | grep -Eo '[0-9]+\.(tcpdump|rustiflow|ifstat)'); do screen -X -S "$session" stuff "^C"; done
```

- And copy files to git repo
  - /data/rustiflow/ifstat.log
  - /data/rustiflow/tcpdump.log
  - /data/rustiflow/rustiflow_realtime_metrics.csv
  - /data/rustiflow/rustiflow.log
  - ~/summary_metrics.csv

Start: 17:10 05/02/2025
ifconfig:

```sh
eno3: flags=4419<UP,BROADCAST,RUNNING,PROMISC,MULTICAST>  mtu 1500
        inet 192.168.0.2  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::ec4:7aff:fe0b:9f76  prefixlen 64  scopeid 0x20<link>
        ether 0c:c4:7a:0b:9f:76  txqueuelen 1000  (Ethernet)
        RX packets 180167478  bytes 213351084960 (213.3 GB)
        RX errors 0  dropped 1141  overruns 0  frame 0
        TX packets 299995801  bytes 431785849888 (431.7 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
