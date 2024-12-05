# RustiFlow-experiments

## Setup Flow feature extractors

### Rustiflow

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

### CICFlowMeter

```sh
sudo apt install openjdk-8-jdk p7zip-full
git clone https://github.com/GintsEngelen/CICFlowMeter.git
cd CICFlowMeter
./gradlew distZip
7z x -y build/distributions/CICFlowMeter-4.0.zip -obuild/distributions
```

### NFStream

```sh
sudo apt install python3-pip
pip install nfstream
```

### Argus

```sh
# sudo apt install gcc make flex bison zlib1g-dev
git clone https://github.com/openargus/argus.git --depth 1
cd argus
LIBS="-lz" ./configure
make
sudo make install
cd ..
git clone https://github.com/openargus/clients.git --depth 1
cd clients
LIBS="-lz" ./configure
make
sudo make install
```

### Go-flows

```sh
wget https://go.dev/dl/go1.23.3.linux-amd64.tar.gz
rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.23.3.linux-amd64.tar.gz
# Add to path (update .bashrc)
export PATH=$PATH:/usr/local/go/bin
git clone https://github.com/CN-TU/go-flows.git
cd go-flows
go build # or go install
```

### Zeek

```sh
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
sudo apt update
sudo apt install zeek
sudo ln -s /opt/zeek/bin/zeek /usr/local/bin/zeek
```

### Joy

```sh
sudo apt install libcurl4-openssl-dev
git clone https://github.com/cisco/joy.git
cd joy
./configure --enable-gzip
make clean
make
sudo ln -s ~/joy/bin/joy /usr/local/bin/joy
```

### nProbe

```sh
sudo add-apt-repository universe
wget https://packages.ntop.org/apt-stable/22.04/all/apt-ntop-stable.deb
sudo apt install ./apt-ntop-stable.deb
sudo apt install nprobe
# Add license [optional]
sudo nano /etc/nprobe.license
```

### Kitsune

See `kitsune_extractor`.

## Prepare PCAPs for Experiments

- Download the pcaps

```sh
# Create data folder
sudo mkdir /data
sudo chown mverkerk /data
cd /data
mkdir monday tuesday wednesday thursday friday

# Download the pcaps (takes ~ 1-2 hours)
wget -O monday/monday.pcap http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/PCAPs/Monday-WorkingHours.pcap
wget -O tuesday/tuesday.pcap http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/PCAPs/Tuesday-WorkingHours.pcap
wget -O wednesday/wednesday.pcap http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/PCAPs/Wednesday-workingHours.pcap
wget -O thursday/thursday.pcap http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/PCAPs/Thursday-WorkingHours.pcap
wget -O friday/friday.pcap http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/PCAPs/Friday-WorkingHours.pcap
```

- Fix and reorder pcaps

```sh
sudo apt install wireshark-common pcapfix
pcapfix /data/monday/monday.pcap
pcapfix /data/tuesday/tuesday.pcap
pcapfix /data/wednesday/wednesday.pcap
pcapfix /data/thursday/thursday.pcap
pcapfix /data/friday/friday.pcap
# Nothing to fix, all was good

reordercap /data/monday/monday.pcap /data/monday/monday-reorder.pcap
# 11709971 frames, 3234 out of order
rm /data/monday/monday.pcap
mv /data/monday/monday-reorder.pcap /data/monday/monday.pcap

reordercap /data/tuesday/tuesday.pcap /data/tuesday/tuesday-reorder.pcap
# 11551954 frames, 3721 out of order
rm /data/tuesday/tuesday.pcap
mv /data/tuesday/tuesday-reorder.pcap /data/tuesday/tuesday.pcap

reordercap /data/wednesday/wednesday.pcap /data/wednesday/wednesday-reorder.pcap
# 13788878 frames, 12654 out of order
rm /data/wednesday/wednesday.pcap
mv /data/wednesday/wednesday-reorder.pcap /data/wednesday/wednesday.pcap

reordercap /data/thursday/thursday.pcap /data/thursday/thursday-reorder.pcap
# 9322025 frames, 3655 out of order
rm /data/thursday/thursday.pcap
mv /data/thursday/thursday-reorder.pcap /data/thursday/thursday.pcap

reordercap /data/friday/friday.pcap /data/friday/friday-reorder.pcap
# 9997874 frames, 7094 out of order
rm /data/friday/friday.pcap
mv /data/friday/friday-reorder.pcap /data/friday/friday.pcap
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

```sh
for session in $(screen -ls | grep -Eo '[0-9]+\.(tcpdump|rustiflow|iftop)'); do screen -X -S "$session" stuff "^C"; done
for session in $(screen -ls | grep -Eo '[0-9]+\.(tcpdump|rustiflow|iftop)'); do screen -X -S "$session" stuff "^C"; done
```

### Copy the files to local

```
~/summary_metrics.csv
~/iftop_data.log
/rustiflow/dump.pcap
/rustiflow/rustiflow_realtime.csv
/rustiflow/rustiflow_realtime_eno1_metrics.csv

zip -j /rustiflow/$(hostname | cut -d '.' -f 1).zip ~/summary_metrics.csv ~/iftop_data.log /rustiflow/dump.pcap /rustiflow/rustiflow_realtime.csv /rustiflow/rustiflow_realtime_eno1_metrics.csv

D:\RustiFlow\scanning-lab\scanning1\node0

zip -j /$(hostname | cut -d '.' -f 1).zip ~/summary_metrics.csv /rustiflow/iftop_data.log /rustiflow/dump.pcap /rustiflow/rustiflow_realtime.csv /rustiflow/rustiflow_realtime_eno1_metrics.csv

D:\RustiFlow\scanning-lab\scanning2
```
