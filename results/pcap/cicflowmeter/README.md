# CICFlowMeter PCAP

## Monday - Friday

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run.sh cicflowmeter
Running test for monday in folder /data/monday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:08:54
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.397979736328125 GB

Running flow exporter on sample_100k...
Executing CMD: ['cfm', '/data/monday/sample_100k.pcap', '/data/monday']
Process ID: 883033
Finished after 0.36923861503601074s

Running flow exporter on sample_500k...
Executing CMD: ['cfm', '/data/monday/sample_500k.pcap', '/data/monday']
Process ID: 883093
Finished after 0.3774688243865967s

Running flow exporter on sample_1M...
Executing CMD: ['cfm', '/data/monday/sample_1M.pcap', '/data/monday']
Process ID: 883153
Finished after 0.3879375457763672s

Running flow exporter on sample_2M...
Executing CMD: ['cfm', '/data/monday/sample_2M.pcap', '/data/monday']
Process ID: 883213
Finished after 0.3960855007171631s

Running flow exporter on sample_4M...
Executing CMD: ['cfm', '/data/monday/sample_4M.pcap', '/data/monday']
Process ID: 883273
Finished after 0.38326096534729004s

Running flow exporter on sample_8M...
Executing CMD: ['cfm', '/data/monday/sample_8M.pcap', '/data/monday']
Process ID: 883333
Finished after 0.36426353454589844s
Test for monday completed successfully.
---------------------------------------------
Running test for tuesday in folder /data/tuesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:08:56
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.40523147583008 GB

Running flow exporter on sample_100k...
Executing CMD: ['cfm', '/data/tuesday/sample_100k.pcap', '/data/tuesday']
Process ID: 883394
Finished after 0.3916330337524414s

Running flow exporter on sample_500k...
Executing CMD: ['cfm', '/data/tuesday/sample_500k.pcap', '/data/tuesday']
Process ID: 883454
Finished after 0.3879852294921875s

Running flow exporter on sample_1M...
Executing CMD: ['cfm', '/data/tuesday/sample_1M.pcap', '/data/tuesday']
Process ID: 883514
Finished after 0.3750460147857666s

Running flow exporter on sample_2M...
Executing CMD: ['cfm', '/data/tuesday/sample_2M.pcap', '/data/tuesday']
Process ID: 883574
Finished after 0.3731687068939209s

Running flow exporter on sample_4M...
Executing CMD: ['cfm', '/data/tuesday/sample_4M.pcap', '/data/tuesday']
Process ID: 883634
Finished after 0.36158013343811035s

Running flow exporter on sample_8M...
Executing CMD: ['cfm', '/data/tuesday/sample_8M.pcap', '/data/tuesday']
Process ID: 883694
Finished after 0.38579297065734863s
Test for tuesday completed successfully.
---------------------------------------------
Running test for wednesday in folder /data/wednesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:08:58
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.40052795410156 GB

Running flow exporter on sample_100k...
Executing CMD: ['cfm', '/data/wednesday/sample_100k.pcap', '/data/wednesday']
Process ID: 883755
Finished after 0.37183475494384766s

Running flow exporter on sample_500k...
Executing CMD: ['cfm', '/data/wednesday/sample_500k.pcap', '/data/wednesday']
Process ID: 883815
^CTraceback (most recent call last):
  File "pcap_performance_test.py", line 161, in <module>
    experiment.run()
  File "pcap_performance_test.py", line 65, in run
    proc.communicate()
  File "/usr/lib/python3.8/subprocess.py", line 1028, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
  File "/usr/lib/python3.8/subprocess.py", line 1868, in _communicate
    ready = selector.select(timeout)
  File "/usr/lib/python3.8/selectors.py", line 415, in select
    fd_event_list = self._selector.poll(timeout)
KeyboardInterrupt

mverkerk@node0:~/RustiFlow-experiments$ cfm /data/tuesday/sample_100k.pcap /data/tuesday
cic.cs.unb.ca.ifm.Cmd You select: /data/tuesday/sample_100k.pcap
cic.cs.unb.ca.ifm.Cmd Out folder: /data/tuesday
cic.cs.unb.ca.ifm.Cmd CICFlowMeter received 1 pcap file
Exception in thread "main" java.lang.UnsatisfiedLinkError: com.slytechs.library.NativeLibrary.dlopen(Ljava/lang/String;)J
        at com.slytechs.library.NativeLibrary.dlopen(Native Method)
        at com.slytechs.library.NativeLibrary.<init>(Unknown Source)
        at com.slytechs.library.JNILibrary.<init>(Unknown Source)
        at com.slytechs.library.JNILibrary.loadLibrary(Unknown Source)
        at com.slytechs.library.JNILibrary.register(Unknown Source)
        at com.slytechs.library.JNILibrary.register(Unknown Source)
        at com.slytechs.library.JNILibrary.register(Unknown Source)
        at org.jnetpcap.Pcap.<clinit>(Unknown Source)
        at cic.cs.unb.ca.jnetpcap.PacketReader.config(PacketReader.java:63)
        at cic.cs.unb.ca.jnetpcap.PacketReader.<init>(PacketReader.java:57)
        at cic.cs.unb.ca.ifm.Cmd.readPcapFile(Cmd.java:128)
        at cic.cs.unb.ca.ifm.Cmd.main(Cmd.java:80)
mverkerk@node0:~/RustiFlow-experiments$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        logs/
        summary_metrics.csv

nothing added to commit but untracked files present (use "git add" to track)
mverkerk@node0:~/RustiFlow-experiments$ rm summary_metrics.csv
mverkerk@node0:~/RustiFlow-experiments$ rm -rf logs/
mverkerk@node0:~/RustiFlow-experiments$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 513 bytes | 513.00 KiB/s, done.
From https://github.com/mielverkerken/RustiFlow-experiments
   732cf21..60b9ef3  main       -> origin/main
Updating 732cf21..60b9ef3
Fast-forward
 pcap_performance_test.py | 9 ++++++---
 1 file changed, 6 insertions(+), 3 deletions(-)
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run.sh cicflowmeter
Running test for monday in folder /data/monday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:16:53
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.40436935424805 GB

Running flow exporter on sample_100k...
Executing CMD: ['./cfm', '/data/monday/sample_100k.pcap', '/data/monday']
Process ID: 883993
Finished after 2.9744553565979004s

Running flow exporter on sample_500k...
Executing CMD: ['./cfm', '/data/monday/sample_500k.pcap', '/data/monday']
Process ID: 884057
Finished after 11.219993591308594s

Running flow exporter on sample_1M...
Executing CMD: ['./cfm', '/data/monday/sample_1M.pcap', '/data/monday']
Process ID: 884123
Finished after 24.67751145362854s

Running flow exporter on sample_2M...
Executing CMD: ['./cfm', '/data/monday/sample_2M.pcap', '/data/monday']
Process ID: 884186
Finished after 58.707443952560425s

Running flow exporter on sample_4M...
Executing CMD: ['./cfm', '/data/monday/sample_4M.pcap', '/data/monday']
Process ID: 884249
Finished after 144.12181615829468s

Running flow exporter on sample_8M...
Executing CMD: ['./cfm', '/data/monday/sample_8M.pcap', '/data/monday']
Process ID: 884318
Finished after 312.3112316131592s
Test for monday completed successfully.
---------------------------------------------
Running test for tuesday in folder /data/tuesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:26:07
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.40528106689453 GB

Running flow exporter on sample_100k...
Executing CMD: ['./cfm', '/data/tuesday/sample_100k.pcap', '/data/tuesday']
Process ID: 884391
Finished after 3.2487854957580566s

Running flow exporter on sample_500k...
Executing CMD: ['./cfm', '/data/tuesday/sample_500k.pcap', '/data/tuesday']
Process ID: 884453
Finished after 11.155999898910522s

Running flow exporter on sample_1M...
Executing CMD: ['./cfm', '/data/tuesday/sample_1M.pcap', '/data/tuesday']
Process ID: 884516
Finished after 24.979873180389404s

Running flow exporter on sample_2M...
Executing CMD: ['./cfm', '/data/tuesday/sample_2M.pcap', '/data/tuesday']
Process ID: 884578
Finished after 57.082645654678345s

Running flow exporter on sample_4M...
Executing CMD: ['./cfm', '/data/tuesday/sample_4M.pcap', '/data/tuesday']
Process ID: 884640
Finished after 150.24859428405762s

Running flow exporter on sample_8M...
Executing CMD: ['./cfm', '/data/tuesday/sample_8M.pcap', '/data/tuesday']
Process ID: 884712
Finished after 347.3061726093292s
Test for tuesday completed successfully.
---------------------------------------------
Running test for wednesday in folder /data/wednesday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:36:01
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.41252517700195 GB

Running flow exporter on sample_100k...
Executing CMD: ['./cfm', '/data/wednesday/sample_100k.pcap', '/data/wednesday']
Process ID: 884787
Finished after 2.451936960220337s

Running flow exporter on sample_500k...
Executing CMD: ['./cfm', '/data/wednesday/sample_500k.pcap', '/data/wednesday']
Process ID: 884849
Finished after 9.735680341720581s

Running flow exporter on sample_1M...
Executing CMD: ['./cfm', '/data/wednesday/sample_1M.pcap', '/data/wednesday']
Process ID: 884960
Finished after 22.165860176086426s

Running flow exporter on sample_2M...
Executing CMD: ['./cfm', '/data/wednesday/sample_2M.pcap', '/data/wednesday']
Process ID: 885022
Finished after 53.47654366493225s

Running flow exporter on sample_4M...
Executing CMD: ['./cfm', '/data/wednesday/sample_4M.pcap', '/data/wednesday']
Process ID: 885107
Finished after 135.559960603714s

Running flow exporter on sample_8M...
Executing CMD: ['./cfm', '/data/wednesday/sample_8M.pcap', '/data/wednesday']
Process ID: 885188
Finished after 275.863569021225s
Test for wednesday completed successfully.
---------------------------------------------
Running test for thursday in folder /data/thursday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:44:21
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.40690994262695 GB

Running flow exporter on sample_100k...
Executing CMD: ['./cfm', '/data/thursday/sample_100k.pcap', '/data/thursday']
Process ID: 885260
Finished after 2.989435911178589s

Running flow exporter on sample_500k...
Executing CMD: ['./cfm', '/data/thursday/sample_500k.pcap', '/data/thursday']
Process ID: 885322
Finished after 11.382647037506104s

Running flow exporter on sample_1M...
Executing CMD: ['./cfm', '/data/thursday/sample_1M.pcap', '/data/thursday']
Process ID: 885384
Finished after 24.28205108642578s

Running flow exporter on sample_2M...
Executing CMD: ['./cfm', '/data/thursday/sample_2M.pcap', '/data/thursday']
Process ID: 885446
Finished after 56.332170248031616s

Running flow exporter on sample_4M...
Executing CMD: ['./cfm', '/data/thursday/sample_4M.pcap', '/data/thursday']
Process ID: 885515
Finished after 138.16293168067932s

Running flow exporter on sample_8M...
Executing CMD: ['./cfm', '/data/thursday/sample_8M.pcap', '/data/thursday']
Process ID: 885580
Finished after 334.9483003616333s
Test for thursday completed successfully.
---------------------------------------------
Running test for friday in folder /data/friday...
Starting pcap performance test with following stats:
Date: 2024-10-08 07:53:49
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.10600662231445 GB
Available Memory: 43.395572662353516 GB

Running flow exporter on sample_100k...
Executing CMD: ['./cfm', '/data/friday/sample_100k.pcap', '/data/friday']
Process ID: 885654
Finished after 3.014559745788574s

Running flow exporter on sample_500k...
Executing CMD: ['./cfm', '/data/friday/sample_500k.pcap', '/data/friday']
Process ID: 885716
Finished after 10.537196636199951s

Running flow exporter on sample_1M...
Executing CMD: ['./cfm', '/data/friday/sample_1M.pcap', '/data/friday']
Process ID: 885778
Finished after 23.180424451828003s

Running flow exporter on sample_2M...
Executing CMD: ['./cfm', '/data/friday/sample_2M.pcap', '/data/friday']
Process ID: 885840
Finished after 54.61291241645813s

Running flow exporter on sample_4M...
Executing CMD: ['./cfm', '/data/friday/sample_4M.pcap', '/data/friday']
Process ID: 885909
Finished after 141.52315163612366s

Running flow exporter on sample_8M...
Executing CMD: ['./cfm', '/data/friday/sample_8M.pcap', '/data/friday']
Process ID: 885972
Finished after 296.61398553848267s
Test for friday completed successfully.
---------------------------------------------
```

### All Days Combined

Flow extraction from cicids2017.pcap (50GB) did not finish within 2 hours.. Was stuck after bit over half milion flows (519579 flows).

-> retry. OOM after 5,5 hours

```sh
mverkerk@node0:~/RustiFlow-experiments$ ./pcap_run_cicids2017.sh cicflowmeter 5
Running test 1 with exporter cicflowmeter...
Starting pcap performance test with following stats:
Date: 2025-02-05 16:17:06
CPU Cores: 16
CPU Logical Cores: 32
Total Memory: 47.09808349609375 GB
Available Memory: 44.16987228393555 GB

Running flow exporter on cicids2017...
Executing CMD: ['./cfm', '/data/cicids2017/cicids2017.pcap', '/data/cicids2017']
Process ID: 1450056
Error occurred while running the command:
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
        at java.util.Arrays.copyOf(Arrays.java:3332)
        at java.lang.AbstractStringBuilder.ensureCapacityInternal(AbstractStringBuilder.java:124)
        at java.lang.AbstractStringBuilder.append(AbstractStringBuilder.java:674)
        at java.lang.StringBuilder.append(StringBuilder.java:213)
        at cic.cs.unb.ca.jnetpcap.BasicPacketInfo.fwdFlowId(BasicPacketInfo.java:78)
        at cic.cs.unb.ca.jnetpcap.FlowGenerator.addPacket(FlowGenerator.java:80)
        at cic.cs.unb.ca.ifm.Cmd.readPcapFile(Cmd.java:167)
        at cic.cs.unb.ca.ifm.Cmd.main(Cmd.java:80)

Finished after 20033.54912996292s
Test 1 complete. Metrics copied to results/pcap/cicflowmeter/cicids2017/1_cicflowmeter_cicids2017_metrics.csv
```
