```sh
mverkerk@node1:~/RustiFlow-experiments$ ./iperf3_run.sh rustiflow eno3
Running test for rustiflow with results in /users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow...
Starting realtime performance test with following stats:
Date: 2025-02-04 04:26:49
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 125.84803009033203 GB
Available Memory: 122.2433967590332 GB

Running flow exporter on interface eno3...
Running with all iperf3 throughputs

Starting test with throughput: 500K
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Process ID: 1433416
                   Finished after 300.1810622215271s

Starting test with throughput: 5M
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Process ID: 1433465
                   Finished after 300.181095123291s

Starting test with throughput: 50M
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Process ID: 1433514
                   Finished after 300.17972588539124s

Starting test with throughput: 500M
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Process ID: 1433569
                   Finished after 300.18052101135254s

Starting test with throughput: 5G
Executing CMD: ['sudo', './rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/users/mverkerk/RustiFlow-experiments/results/realtime/rustiflow/rustiflow_realtime.csv', 'realtime', 'eno3']
Process ID: 1433629
                   Finished after 300.1848418712616s
Test for rustiflow completed successfully.
---------------------------------------------
```
