import sys
import socket
import requests

BANNER = r"""
 ██████╗ ███╗   ███╗███╗   ██╗██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔═══██╗████╗ ████║████╗  ██║██║██╔════╝██╔════╝██╔══██╗████╗  ██║
██║   ██║██╔████╔██║██╔██╗ ██║██║███████╗██║     ███████║██╔██╗ ██║
██║   ██║██║╚██╔╝██║██║╚██╗██║██║╚════██║██║     ██╔══██║██║╚██╗██║
╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║███████║╚██████╗██║  ██║██║ ╚████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
         M R .   M E R C E R  |  U l t i m a t e  S c a n n e r
"""

def validate_ip_or_host(target):
    """Validates the input string to check if it's a valid IP or host."""
    try:
        socket.inet_pton(socket.AF_INET, target)
        return target
    except (socket.error, AttributeError):
        try:
            socket.inet_pton(socket.AF_INET6, target)
            return target
        except socket.error:
            try:
                resolved_ip = socket.gethostbyname(target)
                print(f"[*] Resolved host '{target}' to IP: {resolved_ip}")
                return resolved_ip
            except socket.gaierror:
                return None

def fetch_ip_data(ip_address):
    """Queries an optimized third-party API that accepts browser-like sessions."""
    # Using dynamic configuration endpoint with fallback parameters
    url = f"https://ipwho.is/{ip_address}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }
    
    try:
        # Create an advanced network session context
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=6)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[!] Server responded with status code: {response.status_code}")
            return None
    except requests.exceptions.Timeout:
        print("[!] Network Error: Connection timed out. The server took too long to reply.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"[!] Connection Error: {e}")
        return None

def print_report(data):
    """Formats and prints the extracted network intelligence data safely."""
    if not data or data.get("success") is False:
        error_msg = data.get("message", "Unknown validation error") if data else "No data received"
        print(f"[!] Analysis Failed: {error_msg}")
        return

    print("\n" + "="*50)
    print(f"🌐 TARGET ANALYSIS REPORT FOR: {data.get('ip')}")
    print("="*50)
    
    print(f"📍 Country      : {data.get('country')} ({data.get('country_code')})")
    print(f"🏙️ Region/State : {data.get('region')}")
    print(f"🌆 City         : {data.get('city')}")
    print(f"📮 Postal Code  : {data.get('postal', 'N/A')}")
    print(f"🧭 Coordinates  : Lat {data.get('latitude')}, Lon {data.get('longitude')}")
    
    # Generate clean coordinate-mapping references
    lat, lon = data.get('latitude'), data.get('longitude')
    if lat and lon:
        print(f"🗺️ OpenMap Link  : https://www.openstreetmap.org/#map=12/{lat}/{lon}")
    
    print("-" * 50)
    connection = data.get("connection", {})
    print(f"🏢 Provider/ISP : {connection.get('isp', 'N/A')}")
    print(f"📡 Routing (AS) : {connection.get('asn', 'N/A')}")
    
    timezone = data.get("timezone", {})
    print(f"⏱️ Time Zone    : {timezone.get('id', 'N/A')} ({timezone.get('utc', 'N/A')})")
    print("="*50 + "\n")

def main():
    print(BANNER)
    
    if len(sys.argv) > 1:
        target_input = sys.argv[1]
    else:
        target_input = input("Enter target IP address or Hostname: ").strip()
        
    if not target_input:
        print("[!] Input cannot be empty.")
        sys.exit(1)
        
    target_ip = validate_ip_or_host(target_input)
    if not target_ip:
        print(f"[!] Error: '{target_input}' is not a valid IP address or resolvable domain.")
        sys.exit(1)
        
    print(f"[*] Extracting network intelligence metadata for {target_ip}...")
    report_data = fetch_ip_data(target_ip)
    print_report(report_data)

if __name__ == "__main__":
    main()
