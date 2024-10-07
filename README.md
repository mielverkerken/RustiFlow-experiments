# RustiFlow-experiments

## Setup Virtualwall 2

```sh
git clone https://github.com/idlab-discover/RustiFlow.git
sudo apt install libpcap-dev
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup install stable
rustup toolchain install nightly --component rust-src
cargo install bpf-linker
cd RustiFlow/
cargo xtask ebpf-ipv4 --release
cargo xtask ebpf-ipv6 --release
cargo build --release
sudo ln -s ~/RustiFlow/target/release/rustiflow /usr/local/bin/rustiflow
```

## PCAP Experiments

- PCAP statistics analysis using go script for performance. Python scapy could not handle the big pcap files effectively.
    ```go run pcap_stat.go /data/monday```
- editcap to sample the large PCAP into smaller PCAPs, repeat for monday-friday

    ```sh
    LARGE_PCAP=Monday-WorkingHours.pcap
    OUTPUT=monday
    editcap -r $LARGE_PCAP $OUTPUT/sample_100k.pcap 1-100000
    editcap -r $LARGE_PCAP $OUTPUT/sample_500k.pcap 1-500000
    editcap -r $LARGE_PCAP $OUTPUT/sample_1M.pcap 1-1000000
    editcap -r $LARGE_PCAP $OUTPUT/sample_2M.pcap 1-2000000
    editcap -r $LARGE_PCAP $OUTPUT/sample_4M.pcap 1-4000000
    editcap -r $LARGE_PCAP $OUTPUT/sample_8M.pcap 1-8000000
    ```