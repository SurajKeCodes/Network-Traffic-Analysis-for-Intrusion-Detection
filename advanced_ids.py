# 🛡️ Network Traffic Analysis for Intrusion Detection
# Author: Suraj Borkute

from scapy.all import rdpcap, IP, TCP, UDP
from collections import defaultdict

print("\n🚀 Intrusion Detection System Started...\n")

# Load captured packets (ensure capture.pcap is in same folder)
PCAP_FILE = "capture.pcap"

try:
    packets = rdpcap(PCAP_FILE)
except FileNotFoundError:
    print(f"[ERROR] File '{PCAP_FILE}' not found. Please place it in the project directory.")
    exit()

# Data structures
ip_counter = defaultdict(int)
port_scan = defaultdict(set)
dns_counter = defaultdict(int)

LOG_FILE = "alerts.log"

# Logging function
def log_alert(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

# Detection logic
for pkt in packets:

    if pkt.haslayer(IP):
        src_ip = pkt[IP].src
        ip_counter[src_ip] += 1

        # 🚨 DoS Detection
        if ip_counter[src_ip] > 100:
            alert = f"[ALERT] Possible DoS attack from {src_ip}"
            print(alert)
            log_alert(alert)

        # 🚨 Port Scanning Detection
        if pkt.haslayer(TCP):
            port_scan[src_ip].add(pkt[TCP].dport)

            if len(port_scan[src_ip]) > 15:
                alert = f"[ALERT] Port scanning detected from {src_ip}"
                print(alert)
                log_alert(alert)

        # 🌐 HTTP Traffic Detection
        if pkt.haslayer(TCP) and pkt[TCP].dport == 80:
            print(f"[INFO] HTTP traffic from {src_ip}")

        # 🌍 DNS Traffic Detection
        if pkt.haslayer(UDP) and pkt[UDP].dport == 53:
            dns_counter[src_ip] += 1

            if dns_counter[src_ip] > 20:
                alert = f"[ALERT] High DNS traffic from {src_ip}"
                print(alert)
                log_alert(alert)

# Summary
print("\n📊 Summary:")
print(f"Total unique IPs monitored: {len(ip_counter)}")
print("✅ IDS Analysis Completed\n")
