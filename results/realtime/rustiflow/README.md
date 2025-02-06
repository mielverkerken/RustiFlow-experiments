# Localhost iperf3

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./iperf3_run.sh rustiflow lo 300 127.0.0.1
Running test for rustiflow with results in /users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow...
Starting realtime performance test with following stats:
Date: 2025-02-06 06:26:43
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.09808349609375 GB
Available Memory: 44.30604934692383 GB

Running flow exporter on interface lo...
Running with all iperf3 throughputs

Starting test with throughput: 1M
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/us                                ers/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'lo']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1454608
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish                                ...
   Exporter finished.

                     Finished after 300.24692583084106s

Starting test with throughput: 10M
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/us                                ers/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'lo']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1454680
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish                                ...
   Exporter finished.

                     Finished after 300.29775381088257s

Starting test with throughput: 100M
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/us                                ers/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'lo']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1454752
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish                                ...
   Exporter finished.

                     Finished after 300.3026821613312s

Starting test with throughput: 1G
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/us                                ers/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'lo']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1454831
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.

                                                                                                                                                                                  Finished after 300.2989025115967s

Starting test with throughput: 10G
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'lo']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1454916
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.

                                                                                                                                                                                  Finished after 300.25243520736694s

Starting test with throughput: 0
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'lo']
Waiting for iperf3 client to finish in {self.duration} seconds...
                                                                 Process ID: 1454988
                                                                                    Iperf3 client finished.
                                                                                                           Stopping exporter...
                                                                                                                               Waiting for exporter to finish...
                                                                                                                                                                Exporter finished.

                                                                                                                                                                                  Finished after 300.2967493534088s
Test for rustiflow completed successfully.
---------------------------------------------
```
