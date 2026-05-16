# 🌐 Ultimate IP Metadata Analyzer

A lightweight, robust terminal utility designed for network intelligence gathering and diagnostics. This tool queries high-availability public API endpoints using optimized session handling to extract comprehensive metadata from any valid IPv4/IPv6 address or domain hostname.

Developed by **Mr. Mercer** for terminal-native environments (including Linux CLI and WSL).

---

## 🚀 Features

* **Multi-Format Input:** Seamlessly accepts raw IPv4 addresses, IPv6 addresses, or standard hostnames (e.g., `google.com`).
* **Automated DNS Resolution:** Automatically resolves domains to their underlying public hosting IP addresses before scanning.
* **Deep Network Metrics:** Extracts routing indicators including the Autonomous System Number (ASN) and Internet Service Provider (ISP).
* **Geographic Mapping:** Pulls country, region, city, postal code, timezone, and decimal coordinates.
* **Open-Source Map Integration:** Generates a functional, click-to-navigate OpenStreetMap link based on the target's exact coordinates.
* **Anti-Blocking Optimization:** Utilizes specialized `requests.Session` handling and browser spoofing to bypass generic API scraping filters.

---

## 🛠️ Installation & Setup

Since this tool utilizes the `requests` library for robust session handling, you will need to install the project dependencies first.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MrMercerCybersec-dev/LocTracker.git](https://github.com/MrMercerCybersec-dev/LocTracker.git)

   ```bash
   cd LocTracker
   ```bash
   pip install -r requirements.txt
   ```bash 
   python ip-analyzer.py
