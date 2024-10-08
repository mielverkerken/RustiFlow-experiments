# PCAP Results

Using the pcap_performance_test python script we run the flow extractor tool and capture the resource metrics every second in seperate thread and measure the runtime. The detailed results for each flow exporter are in the subfolders.

Using the `./pcap_run.sh <exporter>` you can execute the experiments on pcap samples of all the days. Then run `./copy_pcap_results.sh <exporter>` to copy the results to the git repository. Finally, run `./pcap_run_cicids2017.sh <exporter> 5` to repeat the same experiment on all days combined (50GB pcap).
