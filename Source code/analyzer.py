import scapy.all as scapy

class NetworkAnalyzer:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.packets = scapy.rdpcap(self.pcap_file)

    def analyze_protocols(self):
        protocol_count = {}
        for packet in self.packets:
            if packet.haslayer(scapy.IP):
                protocol = packet[scapy.IP].proto
                if protocol in protocol_count:
                    protocol_count[protocol] += 1
                else:
                    protocol_count[protocol] = 1
        return protocol_count

    def get_top_talkers(self, n=5):
        ip_count = {}
        for packet in self.packets:
            if packet.haslayer(scapy.IP):
                src_ip = packet[scapy.IP].src
                if src_ip in ip_count:
                    ip_count[src_ip] += 1
                else:
                    ip_count[src_ip] = 1
        return sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:n]