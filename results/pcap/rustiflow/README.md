# RustiFlow PCAP

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run.sh rustiflow
Running test for monday in folder /data/monday...
Starting pcap performance test with following stats:
Date: 2024-10-07 15:50:54
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.04258346557617 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_100k.csv', 'pcap', '/data/monday/sample_100k.pcap']
Process ID: 871214
Finished after 0.16649460792541504s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_500k.csv', 'pcap', '/data/monday/sample_500k.pcap']
Process ID: 871248
Finished after 1.1062052249908447s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_1M.csv', 'pcap', '/data/monday/sample_1M.pcap']
Process ID: 871282
Finished after 2.524383306503296s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_2M.csv', 'pcap', '/data/monday/sample_2M.pcap']
Process ID: 871316
Finished after 5.149806499481201s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_4M.csv', 'pcap', '/data/monday/sample_4M.pcap']
Process ID: 871350
Finished after 12.854406118392944s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_8M.csv', 'pcap', '/data/monday/sample_8M.pcap']
Process ID: 871384
Finished after 29.264506578445435s
Test for monday completed successfully.
---------------------------------------------
Running test for tuesday in folder /data/tuesday...
Starting pcap performance test with following stats:
Date: 2024-10-07 15:51:46
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.04038619995117 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_100k.csv', 'pcap', '/data/tuesday/sample_100k.pcap']
Process ID: 871419
Finished after 0.21272778511047363s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_500k.csv', 'pcap', '/data/tuesday/sample_500k.pcap']
Process ID: 871453
Finished after 1.495194911956787s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_1M.csv', 'pcap', '/data/tuesday/sample_1M.pcap']
Process ID: 871487
Finished after 3.494438886642456s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_2M.csv', 'pcap', '/data/tuesday/sample_2M.pcap']
Process ID: 871521
Finished after 7.4355268478393555s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_4M.csv', 'pcap', '/data/tuesday/sample_4M.pcap']
Process ID: 871557
Finished after 16.773060083389282s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_8M.csv', 'pcap', '/data/tuesday/sample_8M.pcap']
Process ID: 871592
Finished after 26.441498041152954s
Test for tuesday completed successfully.
---------------------------------------------
Running test for wednesday in folder /data/wednesday...
Starting pcap performance test with following stats:
Date: 2024-10-07 15:52:42
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.04169845581055 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_100k.csv', 'pcap', '/data/wednesday/sample_100k.pcap']
Process ID: 871627
Finished after 0.3178596496582031s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_500k.csv', 'pcap', '/data/wednesday/sample_500k.pcap']
Process ID: 871661
Finished after 1.6013295650482178s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_1M.csv', 'pcap', '/data/wednesday/sample_1M.pcap']
Process ID: 871695
Finished after 3.2998197078704834s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_2M.csv', 'pcap', '/data/wednesday/sample_2M.pcap']
Process ID: 871729
Finished after 6.403965950012207s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_4M.csv', 'pcap', '/data/wednesday/sample_4M.pcap']
Process ID: 871763
Finished after 17.584348678588867s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_8M.csv', 'pcap', '/data/wednesday/sample_8M.pcap']
Process ID: 871799
Finished after 28.40266513824463s
Test for wednesday completed successfully.
---------------------------------------------
Running test for thursday in folder /data/thursday...
Starting pcap performance test with following stats:
Date: 2024-10-07 15:53:39
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.0390625 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_100k.csv', 'pcap', '/data/thursday/sample_100k.pcap']
Process ID: 871836
Finished after 0.32364344596862793s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_500k.csv', 'pcap', '/data/thursday/sample_500k.pcap']
Process ID: 871870
Finished after 2.1698286533355713s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_1M.csv', 'pcap', '/data/thursday/sample_1M.pcap']
Process ID: 871904
Finished after 4.293245077133179s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_2M.csv', 'pcap', '/data/thursday/sample_2M.pcap']
Process ID: 871938
Finished after 7.012402534484863s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_4M.csv', 'pcap', '/data/thursday/sample_4M.pcap']
Process ID: 871972
Finished after 13.356477737426758s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_8M.csv', 'pcap', '/data/thursday/sample_8M.pcap']
Process ID: 872006
Finished after 21.16976547241211s
Test for thursday completed successfully.
---------------------------------------------
Running test for friday in folder /data/friday...
Starting pcap performance test with following stats:
Date: 2024-10-07 15:54:28
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.03169631958008 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_100k.csv', 'pcap', '/data/friday/sample_100k.pcap']
Process ID: 872041
Finished after 0.2551119327545166s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_500k.csv', 'pcap', '/data/friday/sample_500k.pcap']
Process ID: 872075
Finished after 1.400146245956421s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_1M.csv', 'pcap', '/data/friday/sample_1M.pcap']
Process ID: 872109
Finished after 3.1585347652435303s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_2M.csv', 'pcap', '/data/friday/sample_2M.pcap']
Process ID: 872143
Finished after 6.274327754974365s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_4M.csv', 'pcap', '/data/friday/sample_4M.pcap']
Process ID: 872177
Finished after 13.177401542663574s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_8M.csv', 'pcap', '/data/friday/sample_8M.pcap']
Process ID: 872211
Finished after 15.3345787525177s
Test for friday completed successfully.
---------------------------------------------
```