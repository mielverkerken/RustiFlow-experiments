# RustiFlow PCAP

## Monday - Friday

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run.sh rustiflow
Running test for monday in folder /data/monday...
Starting pcap performance test with following stats:
Date: 2024-10-08 05:20:31
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.04830551147461 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_100k.csv', 'pcap', '/data/monday/sample_100k.pcap']
Process ID: 877468
Finished after 0.3071732521057129s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_500k.csv', 'pcap', '/data/monday/sample_500k.pcap']
Process ID: 877503
Finished after 1.6439120769500732s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_1M.csv', 'pcap', '/data/monday/sample_1M.pcap']
Process ID: 877539
Finished after 3.8215134143829346s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_2M.csv', 'pcap', '/data/monday/sample_2M.pcap']
Process ID: 877574
Finished after 8.02321982383728s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_4M.csv', 'pcap', '/data/monday/sample_4M.pcap']
Process ID: 877608
Finished after 14.112332344055176s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_8M.csv', 'pcap', '/data/monday/sample_8M.pcap']
Process ID: 877642
Finished after 26.675536394119263s
Test for monday completed successfully.
---------------------------------------------
Running test for tuesday in folder /data/tuesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 05:21:26
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.043418884277344 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_100k.csv', 'pcap', '/data/tuesday/sample_100k.pcap']
Process ID: 877677
Finished after 0.2040879726409912s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_500k.csv', 'pcap', '/data/tuesday/sample_500k.pcap']
Process ID: 877711
Finished after 1.4238851070404053s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_1M.csv', 'pcap', '/data/tuesday/sample_1M.pcap']
Process ID: 877745
Finished after 2.9984381198883057s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_2M.csv', 'pcap', '/data/tuesday/sample_2M.pcap']
Process ID: 877779
Finished after 6.313685417175293s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_4M.csv', 'pcap', '/data/tuesday/sample_4M.pcap']
Process ID: 877813
Finished after 16.369675397872925s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_8M.csv', 'pcap', '/data/tuesday/sample_8M.pcap']
Process ID: 877847
Finished after 26.744990587234497s
Test for tuesday completed successfully.
---------------------------------------------
Running test for wednesday in folder /data/wednesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 05:22:20
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.04451370239258 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_100k.csv', 'pcap', '/data/wednesday/sample_100k.pcap']
Process ID: 877884
Finished after 0.31386470794677734s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_500k.csv', 'pcap', '/data/wednesday/sample_500k.pcap']
Process ID: 877918
Finished after 1.621783971786499s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_1M.csv', 'pcap', '/data/wednesday/sample_1M.pcap']
Process ID: 877952
Finished after 3.727553129196167s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_2M.csv', 'pcap', '/data/wednesday/sample_2M.pcap']
Process ID: 877986
Finished after 6.7362751960754395s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_4M.csv', 'pcap', '/data/wednesday/sample_4M.pcap']
Process ID: 878020
Finished after 14.968999147415161s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_8M.csv', 'pcap', '/data/wednesday/sample_8M.pcap']
Process ID: 878054
Finished after 28.391092777252197s
Test for wednesday completed successfully.
---------------------------------------------
Running test for thursday in folder /data/thursday...
Starting pcap performance test with following stats:
Date: 2024-10-08 05:23:16
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.04774475097656 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_100k.csv', 'pcap', '/data/thursday/sample_100k.pcap']
Process ID: 878092
Finished after 0.25279903411865234s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_500k.csv', 'pcap', '/data/thursday/sample_500k.pcap']
Process ID: 878126
Finished after 1.736645221710205s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_1M.csv', 'pcap', '/data/thursday/sample_1M.pcap']
Process ID: 878160
Finished after 3.5246262550354004s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_2M.csv', 'pcap', '/data/thursday/sample_2M.pcap']
Process ID: 878194
Finished after 7.145060300827026s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_4M.csv', 'pcap', '/data/thursday/sample_4M.pcap']
Process ID: 878228
Finished after 13.422030210494995s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_8M.csv', 'pcap', '/data/thursday/sample_8M.pcap']
Process ID: 878262
Finished after 23.39851403236389s
Test for thursday completed successfully.
---------------------------------------------
Running test for friday in folder /data/friday...
Starting pcap performance test with following stats:
Date: 2024-10-08 05:24:06
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.0426025390625 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_100k.csv', 'pcap', '/data/friday/sample_100k.pcap']
Process ID: 878297
Finished after 0.25693655014038086s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_500k.csv', 'pcap', '/data/friday/sample_500k.pcap']
Process ID: 878331
Finished after 1.4360101222991943s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_1M.csv', 'pcap', '/data/friday/sample_1M.pcap']
Process ID: 878365
Finished after 3.387603282928467s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_2M.csv', 'pcap', '/data/friday/sample_2M.pcap']
Process ID: 878399
Finished after 6.526541233062744s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_4M.csv', 'pcap', '/data/friday/sample_4M.pcap']
Process ID: 878433
Finished after 13.07357120513916s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_8M.csv', 'pcap', '/data/friday/sample_8M.pcap']
Process ID: 878467
Finished after 21.25831365585327s
Test for friday completed successfully.
---------------------------------------------
```

## All Days Combined

5 times repeated

```sh
mverkerk@node0:~/RustiFlow-experiments$ python3 pcap_performance_test.py rustiflow /data/cicids2017 --pcap cicids2017
Starting pcap performance test with following stats:
Date: 2024-10-08 05:27:56
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.05051803588867 GB

Running flow exporter on cicids2017...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/cicids2017/cicids2017.csv', 'pcap', '/data/cicids2017/cicids2017.pcap']
Process ID: 878521
Finished after 168.17799520492554s
mverkerk@node0:~/RustiFlow-experiments$ cp /data/cicids2017/rustiflow_cicids2017_metrics.csv results/pcap/rustiflow/cicids2017/1_rustiflow_cicids2017_metrics.csv
```

```sh
mverkerk@node0:~/RustiFlow-experiments$ python3 pcap_performance_test.py rustiflow /data/cicids2017 --pcap cicids2017
Starting pcap performance test with following stats:
Date: 2024-10-08 05:35:53
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.047752380371094 GB

Running flow exporter on cicids2017...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/cicids2017/cicids2017.csv', 'pcap', '/data/cicids2017/cicids2017.pcap']
Process ID: 878631
Finished after 159.0382535457611s
mverkerk@node0:~/RustiFlow-experiments$ cp /data/cicids2017/rustiflow_cicids2017_metrics.csv results/pcap/rustiflow/cicids2017/2_rustiflow_cicids2017_metrics.csv
```

```sh
mverkerk@node0:~/RustiFlow-experiments$ python3 pcap_performance_test.py rustiflow /data/cicids2017 --pcap cicids2017
Starting pcap performance test with following stats:
Date: 2024-10-08 05:39:53
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.02451705932617 GB

Running flow exporter on cicids2017...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/cicids2017/cicids2017.csv', 'pcap', '/data/cicids2017/cicids2017.pcap']
Process ID: 878747
Finished after 148.76947045326233s
mverkerk@node0:~/RustiFlow-experiments$ cp /data/cicids2017/rustiflow_cicids2017_metrics.csv results/pcap/rustiflow/cicids2017/3_rustiflow_cicids2017_metrics.csv
```

```sh
mverkerk@node0:~/RustiFlow-experiments$ python3 pcap_performance_test.py rustiflow /data/cicids2017 --pcap cicids2017
Starting pcap performance test with following stats:
Date: 2024-10-08 05:42:43
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.03774642944336 GB

Running flow exporter on cicids2017...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/cicids2017/cicids2017.csv', 'pcap', '/data/cicids2017/cicids2017.pcap']
Process ID: 878788
Finished after 147.3885579109192s
mverkerk@node0:~/RustiFlow-experiments$ cp /data/cicids2017/rustiflow_cicids2017_metrics.csv results/pcap/rustiflow/cicids2017/4_rustiflow_cicids2017_metrics.csv
```

```sh
mverkerk@node0:~/RustiFlow-experiments$ python3 pcap_performance_test.py rustiflow /data/cicids2017 --pcap cicids2017
Starting pcap performance test with following stats:
Date: 2024-10-08 05:48:39
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.041404724121094 GB

Running flow exporter on cicids2017...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/cicids2017/cicids2017.csv', 'pcap', '/data/cicids2017/cicids2017.pcap']
Process ID: 878836
Finished after 140.97020745277405s
mverkerk@node0:~/RustiFlow-experiments$ cp /data/cicids2017/rustiflow_cicids2017_metrics.csv results/pcap/rustiflow/cicids2017/5_rustiflow_cicids2017_metrics.csv
```
