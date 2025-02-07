package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
)

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("Usage: %s <folder>", os.Args[0])
	}

	folder := os.Args[1]
	fileNames := []string{"monday/monday", "tuesday/tuesday", "wednesday/wednesday", "thursday/thursday", "friday/friday"}
	// fileNames := []string{"sample_100k", "sample_500k", "sample_1M", "sample_2M", "sample_4M", "sample_8M"}
	// fileNames := []string{"cicids2017"}
	for _, fileName := range fileNames {
		fmt.Println("Processing", fileName)
		pcapFile := fmt.Sprintf("%s/%s.pcap", folder, fileName)
		statFile := fmt.Sprintf("%s/%s_stat.csv", folder, fileName)

		protocolCount, protocolSize, totalPackets, totalSize := processPcapFile(pcapFile)

		displaySummary(protocolCount, protocolSize, totalPackets, totalSize)

		writeToCsv(statFile, protocolCount, protocolSize, totalPackets, totalSize)

		fmt.Println("\nResults have been written to", statFile)
	}
}

// processPcapFile processes the pcap file and returns protocol counts, sizes, and total statistics.
func processPcapFile(pcapFile string) (map[string]int, map[string]int, int, int) {
	handle, err := pcap.OpenOffline(pcapFile)
	if err != nil {
		log.Fatalf("Could not open pcap file: %v", err)
	}
	defer handle.Close()

	packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
	protocolCount := make(map[string]int)
	protocolSize := make(map[string]int)

	totalPackets := 0
	totalSize := 0

	for packet := range packetSource.Packets() {
		totalPackets++
		totalSize += len(packet.Data())

		if totalPackets%100000 == 0 {
			fmt.Printf(".")
		}

		linkLayer := packet.LinkLayer()
		networkLayer := packet.NetworkLayer()
		transportLayer := packet.TransportLayer()

		if networkLayer != nil && transportLayer != nil {
			// Merge network and transport layer (e.g., "IP/TCP", "IP/UDP")
			protocolKey := networkLayer.LayerType().String() + "/" + transportLayer.LayerType().String()
			protocolCount[protocolKey]++
			protocolSize[protocolKey] += len(packet.Data())
		} else if networkLayer != nil {
			// If there's no transport layer, just count the network layer
			proto := networkLayer.LayerType().String()
			protocolCount[proto]++
			protocolSize[proto] += len(packet.Data())
		} else if linkLayer != nil {
			// If there's no network layer, just count the link layer
			proto := linkLayer.LayerType().String()
			protocolCount[proto]++
			protocolSize[proto] += len(packet.Data())
		}
	}
	fmt.Println()

	return protocolCount, protocolSize, totalPackets, totalSize
}

// displaySummary displays the protocol count, size statistics, and the total summary.
func displaySummary(protocolCount map[string]int, protocolSize map[string]int, totalPackets int, totalSize int) {
	fmt.Println("Protocol Summary:")
	for proto, count := range protocolCount {
		size := protocolSize[proto]
		fmt.Printf("Protocol: %s, Count: %d, Size: %d bytes\n", proto, count, size)
	}

	fmt.Println("\nTotal Summary:")
	fmt.Printf("Total Packets: %d\n", totalPackets)
	fmt.Printf("Total Size: %d bytes\n", totalSize)
}

// writeToCsv writes the results to a CSV file.
func writeToCsv(fileName string, protocolCount map[string]int, protocolSize map[string]int, totalPackets int, totalSize int) {
	csvFile, err := os.Create(fileName)
	if err != nil {
		log.Fatalf("Could not create CSV file: %v", err)
	}
	defer csvFile.Close()

	writer := csv.NewWriter(csvFile)
	defer writer.Flush()

	// Write headers
	err = writer.Write([]string{"Protocol", "Count", "Size"})
	if err != nil {
		log.Fatalf("Could not write to CSV file: %v", err)
	}

	// Write protocol data
	for proto, count := range protocolCount {
		size := protocolSize[proto]
		err = writer.Write([]string{proto, strconv.Itoa(count), strconv.Itoa(size)})
		if err != nil {
			log.Fatalf("Could not write to CSV file: %v", err)
		}
	}

	// Write total summary
	err = writer.Write([]string{"Total", strconv.Itoa(totalPackets), strconv.Itoa(totalSize)})
	if err != nil {
		log.Fatalf("Could not write to CSV file: %v", err)
	}
}
