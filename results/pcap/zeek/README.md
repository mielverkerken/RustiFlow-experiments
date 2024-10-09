# Zeek PCAP

/opt/zeek/bin/zeek version 7.0.3

## Monday - Friday

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run.sh zeek
Running test for monday in folder /data/monday...
Starting pcap performance test with following stats:
Date: 2024-10-08 16:48:11
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.063385009765625 GB

Running flow exporter on sample_100k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/monday/sample_100k.pcap']
Process ID: 903709
Finished after 3.1843392848968506s

Running flow exporter on sample_500k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/monday/sample_500k.pcap']
Process ID: 903741
Finished after 7.842835426330566s

Running flow exporter on sample_1M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/monday/sample_1M.pcap']
Process ID: 903774
Finished after 11.860582113265991s

Running flow exporter on sample_2M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/monday/sample_2M.pcap']
Process ID: 903807
Finished after 21.08748149871826s

Running flow exporter on sample_4M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/monday/sample_4M.pcap']
Process ID: 903841
Finished after 40.98586559295654s

Running flow exporter on sample_8M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/monday/sample_8M.pcap']
Process ID: 903874
Finished after 113.64630150794983s
Test for monday completed successfully.
---------------------------------------------
Running test for tuesday in folder /data/tuesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 16:51:30
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.08304214477539 GB

Running flow exporter on sample_100k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/tuesday/sample_100k.pcap']
Process ID: 903914
Finished after 3.3237051963806152s

Running flow exporter on sample_500k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/tuesday/sample_500k.pcap']
Process ID: 903947
Finished after 11.174195528030396s

Running flow exporter on sample_1M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/tuesday/sample_1M.pcap']
Process ID: 903981
Finished after 15.926803350448608s

Running flow exporter on sample_2M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/tuesday/sample_2M.pcap']
Process ID: 904014
Finished after 24.310672521591187s

Running flow exporter on sample_4M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/tuesday/sample_4M.pcap']
Process ID: 904048
Finished after 41.83044791221619s

Running flow exporter on sample_8M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/tuesday/sample_8M.pcap']
Process ID: 904081
Finished after 106.9835753440857s
Test for tuesday completed successfully.
---------------------------------------------
Running test for wednesday in folder /data/wednesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 16:54:53
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.076171875 GB

Running flow exporter on sample_100k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/wednesday/sample_100k.pcap']
Process ID: 904117
Finished after 1.6064963340759277s

Running flow exporter on sample_500k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/wednesday/sample_500k.pcap']
Process ID: 904148
Finished after 5.41649317741394s

Running flow exporter on sample_1M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/wednesday/sample_1M.pcap']
Process ID: 904180
Finished after 9.703938961029053s

Running flow exporter on sample_2M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/wednesday/sample_2M.pcap']
Process ID: 904219
Finished after 18.67058777809143s

Running flow exporter on sample_4M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/wednesday/sample_4M.pcap']
Process ID: 904251
Finished after 36.04303050041199s

Running flow exporter on sample_8M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/wednesday/sample_8M.pcap']
Process ID: 904284
Finished after 122.44504833221436s
Test for wednesday completed successfully.
---------------------------------------------
Running test for thursday in folder /data/thursday...
Starting pcap performance test with following stats:
Date: 2024-10-08 16:58:07
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.08038330078125 GB

Running flow exporter on sample_100k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/thursday/sample_100k.pcap']
Process ID: 904321
Finished after 2.303255319595337s

Running flow exporter on sample_500k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/thursday/sample_500k.pcap']
Process ID: 904355
Finished after 6.708914518356323s

Running flow exporter on sample_1M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/thursday/sample_1M.pcap']
Process ID: 904389
Finished after 11.15047025680542s

Running flow exporter on sample_2M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/thursday/sample_2M.pcap']
Process ID: 904422
Finished after 20.010544061660767s

Running flow exporter on sample_4M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/thursday/sample_4M.pcap']
Process ID: 904455
Finished after 53.6101598739624s

Running flow exporter on sample_8M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/thursday/sample_8M.pcap']
Process ID: 904491
Finished after 137.55901551246643s
Test for thursday completed successfully.
---------------------------------------------
Running test for friday in folder /data/friday...
Starting pcap performance test with following stats:
Date: 2024-10-08 17:01:59
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 44.079017639160156 GB

Running flow exporter on sample_100k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/friday/sample_100k.pcap']
Process ID: 904532
Finished after 2.428009510040283s

Running flow exporter on sample_500k...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/friday/sample_500k.pcap']
Process ID: 904565
Finished after 7.358393907546997s

Running flow exporter on sample_1M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/friday/sample_1M.pcap']
Process ID: 904598
Finished after 10.968608617782593s

Running flow exporter on sample_2M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/friday/sample_2M.pcap']
Process ID: 904632
Finished after 18.009716272354126s

Running flow exporter on sample_4M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/friday/sample_4M.pcap']
Process ID: 904665
Finished after 44.46757769584656s

Running flow exporter on sample_8M...
Executing CMD: ['/opt/zeek/bin/zeek', '-r', '/data/friday/sample_8M.pcap']
Process ID: 904699
Finished after 145.92525482177734s
Test for friday completed successfully.
---------------------------------------------
```

## All Days Combined

5 times repeated

```sh
# shell closed before I could copy output, but all results are saved
```