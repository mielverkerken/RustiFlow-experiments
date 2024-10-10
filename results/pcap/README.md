# PCAP Results

Using the pcap_performance_test python script we run the flow extractor tool and capture the resource metrics every second in seperate thread and measure the runtime. The detailed results for each flow exporter are in the subfolders.

Using the `./pcap_run.sh <exporter>` you can execute the experiments on pcap samples of all the days. Then run `./copy_pcap_results.sh <exporter>` to copy the results to the git repository. Finally, run `./pcap_run_cicids2017.sh <exporter> 5` to repeat the same experiment on all days combined (50GB pcap).

Move the exported flows to git:

```sh
exporter=cicflowmeter
days=("monday" "tuesday" "wednesday" "thursday" "friday")

for day in "${days[@]}"; do
    destination_folder="results/pcap/${exporter}/${day}"
    find "/data/${day}" -name "*.pcap_Flow.csv" -exec mv {} "$destination_folder" \;
done

Single run: `python3 pcap_performance_test.py rustiflow /data/monday --pcap sample_1M`