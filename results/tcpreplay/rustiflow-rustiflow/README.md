```sh
mverkerk@node0:~/RustiFlow-experiments$ ./replay_run.sh rustiflow eno3 300 192.168.0.2
Running test for rustiflow with results in /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow...
Starting realtime performance test with following stats:
Date: 2025-02-23 11:44:22
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.09809112548828 GB
Available Memory: 44.68030548095703 GB

Running flow exporter on interface eno3...
Running with all iperf3 throughputs

Starting test with throughput: 1
Executing CMD: ['sudo', './rustiflow', '-f', 'rustiflow', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--performance-mode', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Starting tcpreplay server: ssh -t mverkerk@192.168.0.2 'exec sudo tcpreplay -i eno3 --duration=300 --mbps=1 --quiet /data/cicids2017/cicids2017-trunc.pcap > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpreplay_server_rustiflow_1.log 2>&1'...
Starting ifstat client: ifstat -i eno3 -n -t 1 > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/ifstat_client_rustiflow_1.log 2>&1...
                                                                                                                                                        Starting tcpdump client: sudo tcpdump --immediate-mode --buffer-size=32768 --packet-buffered -n --interface=eno3 -s 64 -w /dev/null > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpdump_rustiflow_1.log 2>&1...
                                                                     Waiting for server to finish in 300 seconds...
                                                                                                                   Process ID: 334517
                                                                                                                                     Server finished.
Stopping exporter...
Waiting for exporter to finish...
Exporter finished.
Finished after 297.4021100997925s

Starting test with throughput: 10
Executing CMD: ['sudo', './rustiflow', '-f', 'rustiflow', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--performance-mode', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Starting tcpreplay server: ssh -t mverkerk@192.168.0.2 'exec sudo tcpreplay -i eno3 --duration=300 --mbps=10 --quiet /data/cicids2017/cicids2017-trunc.pcap > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpreplay_server_rustiflow_10.log 2>&1'...
Starting ifstat client: ifstat -i eno3 -n -t 1 > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/ifstat_client_rustiflow_10.log 2>&1...
                                                                                                                                                         Starting tcpdump client: sudo tcpdump --immediate-mode --buffer-size=32768 --packet-buffered -n --interface=eno3 -s 64 -w /dev/null > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpdump_rustiflow_10.log 2>&1...
                                                                       Waiting for server to finish in 300 seconds...
                                                                                                                     Process ID: 334568
                                                                                                                                       Server finished.
Stopping exporter...
Waiting for exporter to finish...
Exporter finished.
Finished after 297.3907616138458s

Starting test with throughput: 100
Executing CMD: ['sudo', './rustiflow', '-f', 'rustiflow', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--performance-mode', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Starting tcpreplay server: ssh -t mverkerk@192.168.0.2 'exec sudo tcpreplay -i eno3 --duration=300 --mbps=100 --quiet /data/cicids2017/cicids2017-trunc.pcap > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpreplay_server_rustiflow_100.log 2>&1'...
Starting ifstat client: ifstat -i eno3 -n -t 1 > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/ifstat_client_rustiflow_100.log 2>&1...
                                                                                                                                                          Starting tcpdump client: sudo tcpdump --immediate-mode --buffer-size=32768 --packet-buffered -n --interface=eno3 -s 64 -w /dev/null > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpdump_rustiflow_100.log 2>&1...
                                                                         Waiting for server to finish in 300 seconds...
                                                                                                                       Process ID: 334620
                                                                                                                                         Server finished.
Stopping exporter...
Waiting for exporter to finish...
Exporter finished.
Finished after 297.7082533836365s

Starting test with throughput: 1000
Executing CMD: ['sudo', './rustiflow', '-f', 'rustiflow', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--performance-mode', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Starting tcpreplay server: ssh -t mverkerk@192.168.0.2 'exec sudo tcpreplay -i eno3 --duration=300 --mbps=1000 --quiet /data/cicids2017/cicids2017-trunc.pcap > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpreplay_server_rustiflow_1000.log 2>&1'...
Starting ifstat client: ifstat -i eno3 -n -t 1 > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/ifstat_client_rustiflow_1000.log 2>&1...
                                                                                                                                                           Starting tcpdump client: sudo tcpdump --immediate-mode --buffer-size=32768 --packet-buffered -n --interface=eno3 -s 64 -w /dev/null > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpdump_rustiflow_1000.log 2>&1...
                                                                           Waiting for server to finish in 300 seconds...
                                                                                                                         Process ID: 334676
                                                                                                                                           Server finished.
Stopping exporter...
SIGINT failed, trying SIGTERM...
Waiting for exporter to finish...
Exporter finished.
Error occurred while running the command:
[2025-02-23T18:59:27Z INFO  rustiflow::realtime] Waiting for Ctrl-C...
[2025-02-23T19:02:12Z ERROR rustiflow_ebpf_ipv4] Failed to reserve entry in ring buffer.
[2025-02-23T19:02:12Z ERROR rustiflow_ebpf_ipv4] Failed to reserve entry in ring buffer.
...

Finished after 292.32551741600037s

Starting test with throughput: 10000
Executing CMD: ['sudo', './rustiflow', '-f', 'rustiflow', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--performance-mode', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Starting tcpreplay server: ssh -t mverkerk@192.168.0.2 'exec sudo tcpreplay -i eno3 --duration=300 --mbps=10000 --quiet /data/cicids2017/cicids2017-trunc.pcap > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpreplay_server_rustiflow_10000.log 2>&1'...
Starting ifstat client: ifstat -i eno3 -n -t 1 > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/ifstat_client_rustiflow_10000.log 2>&1...
                                                                                                                                                            Starting tcpdump client: sudo tcpdump --immediate-mode --buffer-size=32768 --packet-buffered -n --interface=eno3 -s 64 -w /dev/null > /users/mverkerk/RustiFlow-experiments/results/tcpreplay/rustiflow/tcpdump_rustiflow_10000.log 2>&1...
                                                                             Waiting for server to finish in 300 seconds...
                                                                                                                           Process ID: 334730
                                                                                                                                             Server finished.
Stopping exporter...
SIGINT failed, trying SIGTERM...
Waiting for exporter to finish...
Exporter finished.
Error occurred while running the command:
[2025-02-23T19:04:22Z INFO  rustiflow::realtime] Waiting for Ctrl-C...
[2025-02-23T19:05:44Z ERROR rustiflow_ebpf_ipv4] Failed to reserve entry in ring buffer.
[2025-02-23T19:05:44Z ERROR rustiflow_ebpf_ipv4] Failed to reserve entry in ring buffer.
[2025-02-23T19:05:44Z ERROR rustiflow_ebpf_ipv4] Failed to reserve entry in ring buffer.
...

Finished after 165.74476981163025s
Test for rustiflow completed successfully.
---------------------------------------------
```
