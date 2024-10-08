# PCAP Results

Using the pcap_performance_test python script we run the flow extractor tool and capture the resource metrics every second in seperate thread and measure the runtime. The detailed results for each flow exporter are in the subfolders.

Using the `pcap_run.sh` you can execute the experiments on pcap samples of all the days. Then run `python3 pcap_performance_test.py <exporter> /data/cicids2017 --pcap cicids2017`. Finally, run `copy_pcap_results.sh` to copy the result files to idlab share.

## PCAP Stats

```sh
mverkerk@node0:~/RustiFlow-experiments$     for day in "${days[@]}"; do
>         go run pcap_stat.go /data/${day}
>     done
Processing sample_100k
.
Protocol Summary:
Protocol: IPv4, Count: 139, Size: 65610 bytes
Protocol: IPv4/UDP, Count: 25330, Size: 3207981 bytes
Protocol: IPv6/UDP, Count: 2817, Size: 412029 bytes
Protocol: IPv6, Count: 754, Size: 62804 bytes
Protocol: IPv4/TCP, Count: 69141, Size: 50844992 bytes
Protocol: Ethernet, Count: 1819, Size: 268873 bytes

Total Summary:
Total Packets: 100000
Total Size: 54862289 bytes

Results have been written to /data/monday/sample_100k_stat.csv
Processing sample_500k
.....
Protocol Summary:
Protocol: IPv4/UDP, Count: 35663, Size: 4517169 bytes
Protocol: IPv6/UDP, Count: 2947, Size: 427408 bytes
Protocol: IPv6, Count: 754, Size: 62804 bytes
Protocol: IPv4/TCP, Count: 458179, Size: 537895000 bytes
Protocol: Ethernet, Count: 2304, Size: 323804 bytes
Protocol: IPv4, Count: 153, Size: 73070 bytes

Total Summary:
Total Packets: 500000
Total Size: 543299255 bytes

Results have been written to /data/monday/sample_500k_stat.csv
Processing sample_1M
..........
Protocol Summary:
Protocol: IPv6/UDP, Count: 3024, Size: 440308 bytes
Protocol: IPv6, Count: 754, Size: 62804 bytes
Protocol: IPv4/TCP, Count: 951800, Size: 1182233093 bytes
Protocol: Ethernet, Count: 2469, Size: 344433 bytes
Protocol: IPv4, Count: 153, Size: 73070 bytes
Protocol: IPv4/UDP, Count: 41800, Size: 8696699 bytes

Total Summary:
Total Packets: 1000000
Total Size: 1191850407 bytes

Results have been written to /data/monday/sample_1M_stat.csv
Processing sample_2M
....................
Protocol Summary:
Protocol: IPv4/TCP, Count: 1942155, Size: 2471598368 bytes
Protocol: Ethernet, Count: 3176, Size: 430169 bytes
Protocol: IPv4, Count: 162, Size: 73612 bytes
Protocol: IPv4/UDP, Count: 50000, Size: 9955490 bytes
Protocol: IPv6/UDP, Count: 3467, Size: 499947 bytes
Protocol: IPv6, Count: 1040, Size: 86776 bytes

Total Summary:
Total Packets: 2000000
Total Size: 2482644362 bytes

Results have been written to /data/monday/sample_2M_stat.csv
Processing sample_4M
........................................
Protocol Summary:
Protocol: IPv6, Count: 1466, Size: 122788 bytes
Protocol: IPv4/TCP, Count: 3894415, Size: 4941276436 bytes
Protocol: Ethernet, Count: 5499, Size: 692334 bytes
Protocol: IPv4, Count: 315, Size: 127178 bytes
Protocol: IPv4/UDP, Count: 92800, Size: 16399549 bytes
Protocol: IPv6/UDP, Count: 5505, Size: 799956 bytes

Total Summary:
Total Packets: 4000000
Total Size: 4959418241 bytes

Results have been written to /data/monday/sample_4M_stat.csv
Processing sample_8M
................................................................................
Protocol Summary:
Protocol: IPv4/TCP, Count: 7546949, Size: 8347615889 bytes
Protocol: Ethernet, Count: 20506, Size: 2372039 bytes
Protocol: IPv4, Count: 941, Size: 292822 bytes
Protocol: IPv4/UDP, Count: 417102, Size: 75742106 bytes
Protocol: IPv6/UDP, Count: 12877, Size: 1925424 bytes
Protocol: IPv6, Count: 1625, Size: 135942 bytes

Total Summary:
Total Packets: 8000000
Total Size: 8428084222 bytes

Results have been written to /data/monday/sample_8M_stat.csv
Processing sample_100k
.
Protocol Summary:
Protocol: Ethernet, Count: 1848, Size: 266617 bytes
Protocol: IPv6/UDP, Count: 2540, Size: 382243 bytes
Protocol: IPv4/TCP, Count: 71119, Size: 47392877 bytes
Protocol: IPv4/UDP, Count: 23658, Size: 3015653 bytes
Protocol: IPv4, Count: 118, Size: 54256 bytes
Protocol: IPv6, Count: 717, Size: 60242 bytes

Total Summary:
Total Packets: 100000
Total Size: 51171888 bytes

Results have been written to /data/tuesday/sample_100k_stat.csv
Processing sample_500k
.....
Protocol Summary:
Protocol: IPv4/UDP, Count: 60027, Size: 7452786 bytes
Protocol: IPv4, Count: 190, Size: 84518 bytes
Protocol: IPv6, Count: 1105, Size: 93114 bytes
Protocol: Ethernet, Count: 3471, Size: 464134 bytes
Protocol: IPv6/UDP, Count: 3904, Size: 607224 bytes
Protocol: IPv4/TCP, Count: 431303, Size: 396968984 bytes

Total Summary:
Total Packets: 500000
Total Size: 405670760 bytes

Results have been written to /data/tuesday/sample_500k_stat.csv
Processing sample_1M
..........
Protocol Summary:
Protocol: IPv4/UDP, Count: 68623, Size: 8468952 bytes
Protocol: IPv4, Count: 190, Size: 84518 bytes
Protocol: IPv6, Count: 1105, Size: 93114 bytes
Protocol: Ethernet, Count: 3653, Size: 485783 bytes
Protocol: IPv6/UDP, Count: 4099, Size: 637553 bytes
Protocol: IPv4/TCP, Count: 922330, Size: 1008278795 bytes

Total Summary:
Total Packets: 1000000
Total Size: 1018048715 bytes

Results have been written to /data/tuesday/sample_1M_stat.csv
Processing sample_2M
....................
Protocol Summary:
Protocol: Ethernet, Count: 3997, Size: 523908 bytes
Protocol: IPv6/UDP, Count: 4125, Size: 641284 bytes
Protocol: IPv4/TCP, Count: 1916999, Size: 2298999804 bytes
Protocol: IPv4/UDP, Count: 73584, Size: 9036921 bytes
Protocol: IPv4, Count: 190, Size: 84518 bytes
Protocol: IPv6, Count: 1105, Size: 93114 bytes

Total Summary:
Total Packets: 2000000
Total Size: 2309379549 bytes

Results have been written to /data/tuesday/sample_2M_stat.csv
Processing sample_4M
........................................
Protocol Summary:
Protocol: IPv4/UDP, Count: 89609, Size: 10892764 bytes
Protocol: IPv4, Count: 206, Size: 94868 bytes
Protocol: IPv6, Count: 1105, Size: 93114 bytes
Protocol: Ethernet, Count: 4710, Size: 600863 bytes
Protocol: IPv6/UDP, Count: 4437, Size: 692205 bytes
Protocol: IPv4/TCP, Count: 3899933, Size: 4826023846 bytes

Total Summary:
Total Packets: 4000000
Total Size: 4838397660 bytes

Results have been written to /data/tuesday/sample_4M_stat.csv
Processing sample_8M
................................................................................
Protocol Summary:
Protocol: IPv6, Count: 1105, Size: 93114 bytes
Protocol: Ethernet, Count: 20044, Size: 2319246 bytes
Protocol: IPv6/UDP, Count: 10755, Size: 1712746 bytes
Protocol: IPv4/TCP, Count: 7611166, Size: 8580201587 bytes
Protocol: IPv4/UDP, Count: 356569, Size: 42145085 bytes
Protocol: IPv4, Count: 361, Size: 183062 bytes

Total Summary:
Total Packets: 8000000
Total Size: 8626654840 bytes

Results have been written to /data/tuesday/sample_8M_stat.csv
Processing sample_100k
.
Protocol Summary:
Protocol: Ethernet, Count: 417, Size: 50441 bytes
Protocol: IPv4/TCP, Count: 94653, Size: 115257595 bytes
Protocol: IPv6/UDP, Count: 495, Size: 77366 bytes
Protocol: IPv4, Count: 23, Size: 13536 bytes
Protocol: IPv4/UDP, Count: 4291, Size: 569970 bytes
Protocol: IPv6, Count: 121, Size: 10318 bytes

Total Summary:
Total Packets: 100000
Total Size: 115979226 bytes

Results have been written to /data/wednesday/sample_100k_stat.csv
Processing sample_500k
.....
Protocol Summary:
Protocol: Ethernet, Count: 606, Size: 71317 bytes
Protocol: IPv4/TCP, Count: 492102, Size: 634929023 bytes
Protocol: IPv6/UDP, Count: 759, Size: 106622 bytes
Protocol: IPv4, Count: 27, Size: 16810 bytes
Protocol: IPv4/UDP, Count: 6385, Size: 857891 bytes
Protocol: IPv6, Count: 121, Size: 10318 bytes

Total Summary:
Total Packets: 500000
Total Size: 635991981 bytes

Results have been written to /data/wednesday/sample_500k_stat.csv
Processing sample_1M
..........
Protocol Summary:
Protocol: IPv4/UDP, Count: 9451, Size: 1249236 bytes
Protocol: IPv6, Count: 121, Size: 10318 bytes
Protocol: Ethernet, Count: 847, Size: 95313 bytes
Protocol: IPv4/TCP, Count: 988547, Size: 1268505949 bytes
Protocol: IPv6/UDP, Count: 999, Size: 147482 bytes
Protocol: IPv4, Count: 35, Size: 23358 bytes

Total Summary:
Total Packets: 1000000
Total Size: 1270031656 bytes

Results have been written to /data/wednesday/sample_1M_stat.csv
Processing sample_2M
....................
Protocol Summary:
Protocol: Ethernet, Count: 1275, Size: 153963 bytes
Protocol: IPv4/TCP, Count: 1979981, Size: 2524761449 bytes
Protocol: IPv6/UDP, Count: 1391, Size: 212166 bytes
Protocol: IPv4, Count: 37, Size: 23500 bytes
Protocol: IPv4/UDP, Count: 17089, Size: 2183210 bytes
Protocol: IPv6, Count: 227, Size: 19274 bytes

Total Summary:
Total Packets: 2000000
Total Size: 2527353562 bytes

Results have been written to /data/wednesday/sample_2M_stat.csv
Processing sample_4M
........................................
Protocol Summary:
Protocol: IPv4/UDP, Count: 28905, Size: 3615418 bytes
Protocol: IPv6, Count: 452, Size: 38224 bytes
Protocol: Ethernet, Count: 2331, Size: 282893 bytes
Protocol: IPv4/TCP, Count: 3965873, Size: 5061543356 bytes
Protocol: IPv6/UDP, Count: 2370, Size: 390493 bytes
Protocol: IPv4, Count: 69, Size: 31910 bytes

Total Summary:
Total Packets: 4000000
Total Size: 5065902294 bytes

Results have been written to /data/wednesday/sample_4M_stat.csv
Processing sample_8M
................................................................................
Protocol Summary:
Protocol: IPv4/UDP, Count: 227069, Size: 26881765 bytes
Protocol: IPv6, Count: 452, Size: 38224 bytes
Protocol: Ethernet, Count: 14944, Size: 1672309 bytes
Protocol: IPv4/TCP, Count: 7749220, Size: 8965191020 bytes
Protocol: IPv6/UDP, Count: 7994, Size: 1285796 bytes
Protocol: IPv4, Count: 321, Size: 127208 bytes

Total Summary:
Total Packets: 8000000
Total Size: 8995196322 bytes

Results have been written to /data/wednesday/sample_8M_stat.csv
Processing sample_100k
.
Protocol Summary:
Protocol: Ethernet, Count: 1335, Size: 204069 bytes
Protocol: IPv4/TCP, Count: 84992, Size: 81088736 bytes
Protocol: IPv4/UDP, Count: 11991, Size: 1594808 bytes
Protocol: IPv6, Count: 578, Size: 48376 bytes
Protocol: IPv6/UDP, Count: 1040, Size: 190117 bytes
Protocol: IPv4, Count: 64, Size: 25900 bytes

Total Summary:
Total Packets: 100000
Total Size: 83152006 bytes

Results have been written to /data/thursday/sample_100k_stat.csv
Processing sample_500k
.....
Protocol Summary:
Protocol: IPv4/UDP, Count: 21988, Size: 2793779 bytes
Protocol: IPv6, Count: 695, Size: 57918 bytes
Protocol: IPv6/UDP, Count: 1788, Size: 289583 bytes
Protocol: IPv4, Count: 77, Size: 35742 bytes
Protocol: Ethernet, Count: 1788, Size: 255881 bytes
Protocol: IPv4/TCP, Count: 473664, Size: 564523061 bytes

Total Summary:
Total Packets: 500000
Total Size: 567955964 bytes

Results have been written to /data/thursday/sample_500k_stat.csv
Processing sample_1M
..........
Protocol Summary:
Protocol: IPv4/UDP, Count: 25510, Size: 3207982 bytes
Protocol: IPv6, Count: 695, Size: 57918 bytes
Protocol: IPv6/UDP, Count: 1983, Size: 306938 bytes
Protocol: IPv4, Count: 97, Size: 52112 bytes
Protocol: Ethernet, Count: 2010, Size: 281122 bytes
Protocol: IPv4/TCP, Count: 969705, Size: 1213830977 bytes

Total Summary:
Total Packets: 1000000
Total Size: 1217737049 bytes

Results have been written to /data/thursday/sample_1M_stat.csv
Processing sample_2M
....................
Protocol Summary:
Protocol: IPv4, Count: 113, Size: 65360 bytes
Protocol: Ethernet, Count: 2503, Size: 333354 bytes
Protocol: IPv4/TCP, Count: 1958502, Size: 2472561156 bytes
Protocol: IPv4/UDP, Count: 35892, Size: 4427052 bytes
Protocol: IPv6, Count: 695, Size: 57918 bytes
Protocol: IPv6/UDP, Count: 2295, Size: 356832 bytes

Total Summary:
Total Packets: 2000000
Total Size: 2477801672 bytes

Results have been written to /data/thursday/sample_2M_stat.csv
Processing sample_4M
........................................
Protocol Summary:
Protocol: Ethernet, Count: 10352, Size: 1217176 bytes
Protocol: IPv4/TCP, Count: 3824947, Size: 4592348998 bytes
Protocol: IPv4/UDP, Count: 157598, Size: 18570863 bytes
Protocol: IPv6, Count: 695, Size: 57918 bytes
Protocol: IPv6/UDP, Count: 6157, Size: 964838 bytes
Protocol: IPv4, Count: 251, Size: 102176 bytes

Total Summary:
Total Packets: 4000000
Total Size: 4613261969 bytes

Results have been written to /data/thursday/sample_4M_stat.csv
Processing sample_8M
................................................................................
Protocol Summary:
Protocol: Ethernet, Count: 41668, Size: 4819567 bytes
Protocol: IPv4/TCP, Count: 7389743, Size: 7211782661 bytes
Protocol: IPv4/UDP, Count: 544520, Size: 63674197 bytes
Protocol: IPv6, Count: 1997, Size: 173166 bytes
Protocol: IPv6/UDP, Count: 21003, Size: 3308232 bytes
Protocol: IPv4, Count: 1069, Size: 248758 bytes

Total Summary:
Total Packets: 8000000
Total Size: 7284006581 bytes

Results have been written to /data/thursday/sample_8M_stat.csv
Processing sample_100k
.
Protocol Summary:
Protocol: IPv6, Count: 793, Size: 66354 bytes
Protocol: IPv4, Count: 57, Size: 16344 bytes
Protocol: IPv4/UDP, Count: 13247, Size: 1741444 bytes
Protocol: Ethernet, Count: 1375, Size: 202098 bytes
Protocol: IPv4/TCP, Count: 83287, Size: 79460742 bytes
Protocol: IPv6/UDP, Count: 1241, Size: 201545 bytes

Total Summary:
Total Packets: 100000
Total Size: 81688527 bytes

Results have been written to /data/friday/sample_100k_stat.csv
Processing sample_500k
.....
Protocol Summary:
Protocol: Ethernet, Count: 2509, Size: 331731 bytes
Protocol: IPv4/TCP, Count: 464126, Size: 523629409 bytes
Protocol: IPv6/UDP, Count: 2820, Size: 407637 bytes
Protocol: IPv6, Count: 1014, Size: 85568 bytes
Protocol: IPv4, Count: 105, Size: 47096 bytes
Protocol: IPv4/UDP, Count: 29426, Size: 3705156 bytes

Total Summary:
Total Packets: 500000
Total Size: 528206597 bytes

Results have been written to /data/friday/sample_500k_stat.csv
Processing sample_1M
..........
Protocol Summary:
Protocol: IPv6, Count: 1014, Size: 85568 bytes
Protocol: IPv4, Count: 105, Size: 47096 bytes
Protocol: IPv4/UDP, Count: 31984, Size: 3999684 bytes
Protocol: Ethernet, Count: 2770, Size: 358915 bytes
Protocol: IPv4/TCP, Count: 961274, Size: 1154846821 bytes
Protocol: IPv6/UDP, Count: 2853, Size: 411054 bytes

Total Summary:
Total Packets: 1000000
Total Size: 1159749138 bytes

Results have been written to /data/friday/sample_1M_stat.csv
Processing sample_2M
....................
Protocol Summary:
Protocol: IPv4/TCP, Count: 1956863, Size: 2433082738 bytes
Protocol: IPv6/UDP, Count: 3139, Size: 457490 bytes
Protocol: IPv6, Count: 1014, Size: 85568 bytes
Protocol: IPv4, Count: 105, Size: 47096 bytes
Protocol: IPv4/UDP, Count: 35673, Size: 4430874 bytes
Protocol: Ethernet, Count: 3206, Size: 408123 bytes

Total Summary:
Total Packets: 2000000
Total Size: 2438511889 bytes

Results have been written to /data/friday/sample_2M_stat.csv
Processing sample_4M
........................................
Protocol Summary:
Protocol: Ethernet, Count: 8518, Size: 982758 bytes
Protocol: IPv4/TCP, Count: 3859401, Size: 4641333273 bytes
Protocol: IPv6/UDP, Count: 6362, Size: 925145 bytes
Protocol: IPv6, Count: 1014, Size: 85568 bytes
Protocol: IPv4, Count: 154, Size: 80990 bytes
Protocol: IPv4/UDP, Count: 124551, Size: 15158400 bytes

Total Summary:
Total Packets: 4000000
Total Size: 4658566134 bytes

Results have been written to /data/friday/sample_4M_stat.csv
Processing sample_8M
................................................................................
Protocol Summary:
Protocol: IPv6/UDP, Count: 23339, Size: 3574479 bytes
Protocol: IPv6, Count: 1014, Size: 85568 bytes
Protocol: IPv4, Count: 919, Size: 309583 bytes
Protocol: IPv4/UDP, Count: 612891, Size: 73535874 bytes
Protocol: IPv4/SCTP, Count: 62, Size: 4092 bytes
Protocol: Ethernet, Count: 44738, Size: 5060229 bytes
Protocol: IPv4/TCP, Count: 7317037, Size: 6840690344 bytes

Total Summary:
Total Packets: 8000000
Total Size: 6923260169 bytes

Results have been written to /data/friday/sample_8M_stat.csv
```