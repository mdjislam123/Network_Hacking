import scapy.all as scapy
import argparse
import socket

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--network", dest="network", help="The network range to scan")
    options = parser.parse_args()
    if not options.network:
        parser.error("[-] Please specify a network range, use --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    for element in answered_list:
        print("IP: " + element[1].psrc + "\tMAC: " + element[1].hwsrc)
        try:
            host_name = socket.gethostbyaddr(element[1].psrc)[0]
            print(f"Hostname:  {host_name}\n")
        except socket.herror:
            print("Hostname: Could not be resolved\n")

    print("\nScan completed")

options = get_arguments()
scan(options.network)
