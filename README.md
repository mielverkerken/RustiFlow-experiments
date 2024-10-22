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

## Prepare PCAPs for Experiments

- reorder caps to make pcap files ordered
    ```sh
        reordercap /data/monday/Monday-WorkingHours.pcap /data/monday/monday.pcap
        # 11709971 frames, 3234 out of order
        reordercap /data/tuesday/Tuesday-WorkingHours.pcap /data/tuesday/tuesday.pcap
        # 11551954 frames, 3721 out of order
        reordercap /data/wednesday/Wednesday-WorkingHours.pcap /data/wednesday/wednesday.pcap
        # 13788878 frames, 12654 out of order
        reordercap /data/thursday/Thursday-WorkingHours.pcap /data/thursday/thursday.pcap
        # 9322025 frames, 3655 out of order
        reordercap /data/friday/Friday-WorkingHours.pcap /data/friday/friday.pcap
        # 9997874 frames, 7094 out of order
    ```

- editcap to sample the large PCAP into smaller PCAPs, repeat for monday-friday
    ```sh
    days=("monday" "tuesday" "wednesday" "thursday" "friday")

    for day in "${days[@]}"; do
        editcap -r /data/${day}/${day}.pcap /data/${day}/sample_100k.pcap 1-100000
        editcap -r /data/${day}/${day}.pcap /data/${day}/sample_500k.pcap 1-500000
        editcap -r /data/${day}/${day}.pcap /data/${day}/sample_1M.pcap 1-1000000
        editcap -r /data/${day}/${day}.pcap /data/${day}/sample_2M.pcap 1-2000000
        editcap -r /data/${day}/${day}.pcap /data/${day}/sample_4M.pcap 1-4000000
        editcap -r /data/${day}/${day}.pcap /data/${day}/sample_8M.pcap 1-8000000
    done
    ```

- PCAP statistics analysis using go script for performance. Python scapy could not handle the big pcap files effectively.
    ```sh
    days=("monday" "tuesday" "wednesday" "thursday" "friday")

    for day in "${days[@]}"; do
        go run pcap_stat.go /data/${day}
    done
    ```

- Merge all pcaps to create `cicids2017.pcap` and also compute stats
    ```sh
    mergecap -a -F pcapng -v -w /data/cicids2017/cicids2017.pcap  /data/monday/monday.pcap /data/tuesday/tuesday.pcap /data/wednesday/wednesday.pcap /data/thursday/thursday.pcap /data/friday/friday.pcap
    # change filenames in pcap_stat.go (change commented out code)
    go run pcap_stat.go /data/cicids2017
    ```

## Setup Virtualwall

```sh
#!/bin/bash -e
curl https://sh.rustup.rs -sSf | sh -s -- -y
```

```sh
#!/bin/bash -e
/users/mverkerk/.cargo/bin/rustup install stable
/users/mverkerk/.cargo/bin/rustup toolchain install nightly --component rust-src
/users/mverkerk/.cargo/bin/cargo install bpf-linker
git clone https://github.com/idlab-discover/RustiFlow.git
cd RustiFlow/
/users/mverkerk/.cargo/bin/cargo xtask ebpf-ipv4 --release
/users/mverkerk/.cargo/bin/cargo xtask ebpf-ipv6 --release
sudo apt install libpcap-dev -y
/users/mverkerk/.cargo/bin/cargo build --release
cd ..
git clone https://github.com/mielverkerken/RustiFlow-experiments
cd RustiFlow-experiments
sudo apt install python3-pip -y
pip install -r requirements.txt --break-system-package
sudo mkdir /rustiflow
sudo chown mverkerk /rustiflow
sudo apt install screen iftop -y
```

```sh
screen -dmS tcpdump bash -c "sudo tcpdump -i eno1 -n -w /rustiflow/dump.pcap"
screen -dmS rustiflow bash -c "python3 /users/mverkerk/RustiFlow-experiments/realtime_performance_test.py rustiflow /rustiflow --interface eno1"
cd /rustiflow
screen -dmS iftop bash -c "/users/mverkerk/RustiFlow-experiments/collect_iftop_data.sh eno1"
```