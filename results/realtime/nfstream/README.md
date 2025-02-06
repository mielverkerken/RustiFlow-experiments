# Iperf3 localhost

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./iperf3_run.sh nfstream lo 300 127.0.0.1
Running test for nfstream with results in /users/mverkerk/RustiFlow-experiments/results/realtime/nfstream...
Starting realtime performance test with following stats:
Date: 2025-02-06 07:01:31
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.09808349609375 GB
Available Memory: 44.2909049987793 GB

Running flow exporter on interface lo...
Running with all iperf3 throughputs

Starting test with throughput: 1M
Executing CMD: ['python3', '/users/mverkerk/RustiFlow-experiments/nfstream_script.py', '--realtime', 'lo.pcap', '--output', '/users/mverkerk/RustiFlow-experiments/results/realtime/nfstream']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1455129
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.
                                                                                                                                                                                  NFStream processing in real-time on interface: lo.pcap

                                           Error occurred while running the command:
                                                                                    Traceback (most recent call last):
                                                                                                                        File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 59, in <module>
                    process_realtime(args.realtime, args.output)
                                                                  File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 27, in process_realtime
                                                                                                                                                                   my_streamer = NFStreamer(source=interface,
                  File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 78, in __init__
                                                                                                                           self.source = source
                                                                                                                                                 File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 132, in source
                                                            raise ValueError("Please specify a pcap file path or a valid network interface name as source.")
                                                                                                                                                            ValueError: Please specify a pcap file path or a valid network interface name as source.

                                                       Finished after 300.1870844364166s

Starting test with throughput: 10M
Executing CMD: ['python3', '/users/mverkerk/RustiFlow-experiments/nfstream_script.py', '--realtime', 'lo.pcap', '--output', '/users/mverkerk/RustiFlow-experiments/results/realtime/nfstream']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1455196
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.
                                                                                                                                                                                  NFStream processing in real-time on interface: lo.pcap

                                           Error occurred while running the command:
                                                                                    Traceback (most recent call last):
                                                                                                                        File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 59, in <module>
                    process_realtime(args.realtime, args.output)
                                                                  File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 27, in process_realtime
                                                                                                                                                                   my_streamer = NFStreamer(source=interface,
                  File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 78, in __init__
                                                                                                                           self.source = source
                                                                                                                                                 File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 132, in source
                                                            raise ValueError("Please specify a pcap file path or a valid network interface name as source.")
                                                                                                                                                            ValueError: Please specify a pcap file path or a valid network interface name as source.

                                                       Finished after 300.18344259262085s

Starting test with throughput: 100M
Executing CMD: ['python3', '/users/mverkerk/RustiFlow-experiments/nfstream_script.py', '--realtime', 'lo.pcap', '--output', '/users/mverkerk/RustiFlow-experiments/results/realtime/nfstream']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1455263
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.
                                                                                                                                                                                  NFStream processing in real-time on interface: lo.pcap

                                           Error occurred while running the command:
                                                                                    Traceback (most recent call last):
                                                                                                                        File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 59, in <module>
                    process_realtime(args.realtime, args.output)
                                                                  File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 27, in process_realtime
                                                                                                                                                                   my_streamer = NFStreamer(source=interface,
                  File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 78, in __init__
                                                                                                                           self.source = source
                                                                                                                                                 File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 132, in source
                                                            raise ValueError("Please specify a pcap file path or a valid network interface name as source.")
                                                                                                                                                            ValueError: Please specify a pcap file path or a valid network interface name as source.

                                                       Finished after 300.1903681755066s

Starting test with throughput: 1G
Executing CMD: ['python3', '/users/mverkerk/RustiFlow-experiments/nfstream_script.py', '--realtime', 'lo.pcap', '--output', '/users/mverkerk/RustiFlow-experiments/results/realtime/nfstream']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1455335
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.
                                                                                                                                                                                  NFStream processing in real-time on interface: lo.pcap

                                           Error occurred while running the command:
                                                                                    Traceback (most recent call last):
                                                                                                                        File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 59, in <module>
                    process_realtime(args.realtime, args.output)
                                                                  File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 27, in process_realtime
                                                                                                                                                                   my_streamer = NFStreamer(source=interface,
                  File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 78, in __init__
                                                                                                                           self.source = source
                                                                                                                                                 File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 132, in source
                                                            raise ValueError("Please specify a pcap file path or a valid network interface name as source.")
                                                                                                                                                            ValueError: Please specify a pcap file path or a valid network interface name as source.

                                                       Finished after 300.1839597225189s

Starting test with throughput: 10G
Executing CMD: ['python3', '/users/mverkerk/RustiFlow-experiments/nfstream_script.py', '--realtime', 'lo.pcap', '--output', '/users/mverkerk/RustiFlow-experiments/results/realtime/nfstream']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1455404
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.
                                                                                                                                                                                  NFStream processing in real-time on interface: lo.pcap

                                           Error occurred while running the command:
                                                                                    Traceback (most recent call last):
                                                                                                                        File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 59, in <module>
                    process_realtime(args.realtime, args.output)
                                                                  File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 27, in process_realtime
                                                                                                                                                                   my_streamer = NFStreamer(source=interface,
                  File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 78, in __init__
                                                                                                                           self.source = source
                                                                                                                                                 File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 132, in source
                                                            raise ValueError("Please specify a pcap file path or a valid network interface name as source.")
                                                                                                                                                            ValueError: Please specify a pcap file path or a valid network interface name as source.

                                                       Finished after 300.19050455093384s

Starting test with throughput: 0
Executing CMD: ['python3', '/users/mverkerk/RustiFlow-experiments/nfstream_script.py', '--realtime', 'lo.pcap', '--output', '/users/mverkerk/RustiFlow-experiments/results/realtime/nfstream']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1455472
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.
                                                                                                                                                                                  NFStream processing in real-time on interface: lo.pcap

                                           Error occurred while running the command:
                                                                                    Traceback (most recent call last):
                                                                                                                        File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 59, in <module>
                    process_realtime(args.realtime, args.output)
                                                                  File "/users/mverkerk/RustiFlow-experiments/nfstream_script.py", line 27, in process_realtime
                                                                                                                                                                   my_streamer = NFStreamer(source=interface,
                  File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 78, in __init__
                                                                                                                           self.source = source
                                                                                                                                                 File "/users/mverkerk/.local/lib/python3.10/site-packages/nfstream/streamer.py", line 132, in source
                                                            raise ValueError("Please specify a pcap file path or a valid network interface name as source.")
                                                                                                                                                            ValueError: Please specify a pcap file path or a valid network interface name as source.

                                                       Finished after 300.1808578968048s
Test for nfstream completed successfully.
---------------------------------------------
```
