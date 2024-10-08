# RustiFlow PCAP

## Monday - Friday

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run.sh rustiflow
Running test for monday in folder /data/monday...
Starting pcap performance test with following stats:
Date: 2024-10-07 18:32:20
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.03165054321289 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_100k.csv', 'pcap', '/data/monday/sample_100k.pcap']
Process ID: 874641
Finished after 0.2542438507080078s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_500k.csv', 'pcap', '/data/monday/sample_500k.pcap']
Process ID: 874675
Finished after 1.644132375717163s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_1M.csv', 'pcap', '/data/monday/sample_1M.pcap']
Process ID: 874709
Finished after 3.8597304821014404s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_2M.csv', 'pcap', '/data/monday/sample_2M.pcap']
Process ID: 874743
Finished after 7.705474138259888s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_4M.csv', 'pcap', '/data/monday/sample_4M.pcap']
Process ID: 874777
Finished after 14.01293420791626s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/monday/sample_8M.csv', 'pcap', '/data/monday/sample_8M.pcap']
Process ID: 874811
Finished after 26.44620656967163s
Test for monday completed successfully.
---------------------------------------------
Running test for tuesday in folder /data/tuesday...
Starting pcap performance test with following stats:
Date: 2024-10-07 18:33:14
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.033424377441406 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_100k.csv', 'pcap', '/data/tuesday/sample_100k.pcap']
Process ID: 874847
Finished after 0.21500086784362793s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_500k.csv', 'pcap', '/data/tuesday/sample_500k.pcap']
Process ID: 874881
Finished after 1.3999857902526855s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_1M.csv', 'pcap', '/data/tuesday/sample_1M.pcap']
Process ID: 874915
Finished after 2.987299680709839s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_2M.csv', 'pcap', '/data/tuesday/sample_2M.pcap']
Process ID: 874949
Finished after 6.26996636390686s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_4M.csv', 'pcap', '/data/tuesday/sample_4M.pcap']
Process ID: 874983
Finished after 14.188730478286743s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/tuesday/sample_8M.csv', 'pcap', '/data/tuesday/sample_8M.pcap']
Process ID: 875017
Finished after 26.79487919807434s
Test for tuesday completed successfully.
---------------------------------------------
Running test for wednesday in folder /data/wednesday...
Starting pcap performance test with following stats:
Date: 2024-10-07 18:34:06
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.036582946777344 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_100k.csv', 'pcap', '/data/wednesday/sample_100k.pcap']
Process ID: 875052
Finished after 0.31641411781311035s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_500k.csv', 'pcap', '/data/wednesday/sample_500k.pcap']
Process ID: 875086
Finished after 1.6233406066894531s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_1M.csv', 'pcap', '/data/wednesday/sample_1M.pcap']
Process ID: 875120
Finished after 3.6347572803497314s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_2M.csv', 'pcap', '/data/wednesday/sample_2M.pcap']
Process ID: 875154
Finished after 6.665082216262817s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_4M.csv', 'pcap', '/data/wednesday/sample_4M.pcap']
Process ID: 875188
Finished after 14.921782732009888s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/wednesday/sample_8M.csv', 'pcap', '/data/wednesday/sample_8M.pcap']
Process ID: 875222
Finished after 27.961376428604126s
Test for wednesday completed successfully.
---------------------------------------------
Running test for thursday in folder /data/thursday...
Starting pcap performance test with following stats:
Date: 2024-10-07 18:35:01
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.03505325317383 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_100k.csv', 'pcap', '/data/thursday/sample_100k.pcap']
Process ID: 875265
Finished after 0.24919986724853516s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_500k.csv', 'pcap', '/data/thursday/sample_500k.pcap']
Process ID: 875299
Finished after 1.7760868072509766s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_1M.csv', 'pcap', '/data/thursday/sample_1M.pcap']
Process ID: 875333
Finished after 3.296557903289795s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_2M.csv', 'pcap', '/data/thursday/sample_2M.pcap']
Process ID: 875367
Finished after 7.135028123855591s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_4M.csv', 'pcap', '/data/thursday/sample_4M.pcap']
Process ID: 875402
Finished after 13.345176219940186s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/thursday/sample_8M.csv', 'pcap', '/data/thursday/sample_8M.pcap']
Process ID: 875436
Finished after 23.237330675125122s
Test for thursday completed successfully.
---------------------------------------------
Running test for friday in folder /data/friday...
Starting pcap performance test with following stats:
Date: 2024-10-07 18:35:50
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.03082275390625 GB

Running flow exporter on sample_100k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_100k.csv', 'pcap', '/data/friday/sample_100k.pcap']
Process ID: 875471
Finished after 0.25650739669799805s

Running flow exporter on sample_500k...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_500k.csv', 'pcap', '/data/friday/sample_500k.pcap']
Process ID: 875505
Finished after 1.533372163772583s

Running flow exporter on sample_1M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_1M.csv', 'pcap', '/data/friday/sample_1M.pcap']
Process ID: 875539
Finished after 3.30914044380188s

Running flow exporter on sample_2M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_2M.csv', 'pcap', '/data/friday/sample_2M.pcap']
Process ID: 875573
Finished after 6.578695297241211s

Running flow exporter on sample_4M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_4M.csv', 'pcap', '/data/friday/sample_4M.pcap']
Process ID: 875607
Finished after 13.098365068435669s

Running flow exporter on sample_8M...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/friday/sample_8M.csv', 'pcap', '/data/friday/sample_8M.pcap']
Process ID: 875641
Finished after 22.98902678489685s
Test for friday completed successfully.
---------------------------------------------
```

## All Days Combined

```sh
mverkerk@node0:~/RustiFlow-experiments$ python3 pcap_performance_test.py rustiflow /data/cicids2017 --pcap cicids2017
Starting pcap performance test with following stats:
Date: 2024-10-07 18:38:35
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.03579330444336 GB

Running flow exporter on cicids2017...
Executing CMD: ['rustiflow', '-f', 'cic', '--header', '--idle-timeout', '120', '--active-timeout', '3600', '--output', 'csv', '--export-path', '/data/cicids2017/cicids2017.csv', 'pcap', '/data/cicids2017/cicids2017.pcap']
Process ID: 875680
Finished after 164.2532126903534s
```
