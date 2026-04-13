# 🛡️ Network Traffic Analysis for Intrusion Detection

A practical cybersecurity project focused on capturing real network traffic using Wireshark and performing packet-level analysis using a Python-based Intrusion Detection System (IDS). The system identifies anomalous and potentially malicious activities such as DoS attacks, port scanning, and DNS-based irregularities.

---

## 📌 Overview

This project demonstrates a complete **network security workflow**:

**Capture → Analyze → Detect → Alert**

* 📡 Capture real network traffic using Wireshark
* 🧠 Perform packet-level analysis using Python (Scapy)
* 🚨 Detect anomalous and suspicious patterns
* 📝 Log alerts for further investigation



## 🏗️ Architecture

<h2 align="center"></h2>

<p align="center">
  <img src="https://github.com/user-attachments/assets/2c497848-c0a0-4428-8ff1-d27f446b2334"
       width="500"
       style="border: 2px solid #444; border-radius: 10px; padding: 5px;" />
</p>

---

## ✨ Key Features

* 🚨 Detection of **DoS (Denial of Service) patterns**
* 🔍 Identification of **Port Scanning activities**
* 🌐 Monitoring of **HTTP traffic (plaintext exposure)**
* 🌍 Detection of **DNS anomalies and high-frequency queries**
* 📝 Alert logging in `alerts.log`
* ⚡ Efficient offline packet analysis

---

## ⚙️ Tech Stack

* Kali Linux
* Wireshark
* Python
* Scapy (Packet Analysis Library)
* Networking Protocols: TCP/IP, DNS, HTTP

---

## 📸 Project Screenshots

<h3 align="center">📡 Packet Capture & HTTP Analysis</h3>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/60b79794-0fb1-4b56-9f81-678e295032b8" width="450"/>
      <br><b>Packet Capture</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/a6823ca9-11da-451a-8306-0175426f2e7c" width="450"/>
      <br><b>HTTP Analysis</b>
    </td>
  </tr>
</table>

---

<h3 align="center">🌍 DNS Analysis </h3>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/650191ba-1956-46ce-b37d-8f0fbd1eb090" width="450"/>
      <br><b>Packet Capture</b>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f37423ad-177d-4fe7-9ff8-d5b09d5497f2" width="450"/>
      <br><b>DNS Analysis</b>
    </td>
  </tr>
</table>

---

<h3 align="center">🛡️ IDS Output & Summary</h3>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/ad6f17f8-7b4a-48f6-a901-7c34f0f3df9d" width="500"/>
      <br><b>TCP Stream</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/2f3dcc26-7c5c-4ec8-9538-633552a7ef51" width="500"/>
      <br><b> IDS Output Summary</b>
    </td>
  </tr>
</table>

---

---

## 🔧 Setup & Execution

### 1. Capture Network Traffic

* Open Wireshark
* Select `eth0` interface
* Start packet capture
* Generate traffic (web browsing, ping, etc.)
* Save capture file as `capture.pcap`

---

### 2. Run IDS Script

```bash
cd Advanced-IDS
python3 advanced_ids.py
```

---

## ⚔️ Detection Capabilities

The IDS performs:

* 🚨 High packet rate analysis → Potential DoS detection
* 🚨 Multi-port access tracking → Port scan detection
* 🌐 HTTP inspection → Identification of unencrypted communication
* 🌍 DNS monitoring → Detection of abnormal query patterns

---

## 📊 Sample Output

```
[INFO] HTTP traffic from 192.168.x.x
[ALERT] Possible DoS attack from 192.168.x.x
[ALERT] High DNS traffic from 192.168.x.x

📊 Summary:
Total IPs monitored: X
```

---

## 🧠 Key Learnings

* Understanding of network protocols (TCP, DNS, HTTP)
* Packet-level traffic inspection and analysis
* Identification of anomalous network behavior
* Development of custom intrusion detection logic
* Security implications of unencrypted communication

---

## 🚀 Future Improvements

* Real-time IDS using live packet sniffing
* Integration with SIEM tools for centralized logging
* Machine learning-based anomaly detection
* Visualization dashboard for traffic insights
* Automated alerting (Email / Telegram integration)

---

## 👨‍💻 Author

**Suraj Borkute**
Cybersecurity Enthusiast | Networking | GATE Aspirant 🚀

---

## 🤝 Connect With Me

* 🔗 LinkedIn: https://www.linkedin.com/in/suraj-borkute
* 💻 GitHub: https://github.com/SurajKeCodes
* 🌐 Portfolio: https://suraj-borkute-portfolio.vercel.app

---

## ⚠️ Disclaimer

This project is intended for educational purposes only.
All experiments were conducted in a controlled environment.

---

## 📄 License

This project is licensed under the MIT License.
