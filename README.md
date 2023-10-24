# Include your final research, documentation, code developed, and code demos. 
## **Research on technology background**

### Docker Apache httpd vs. Python Flask Library

Docker Apache httpd and Python Flask are two distinct technologies used in web development, each playing a unique role in the web application stack. Docker Apache httpd involves hosting the Apache HTTP server within a Docker container, providing a self-contained environment for deploying web applications easily and consistently across different environments. This containerization approach allows for horizontal scaling and efficient load balancing, making it suitable for projects requiring scalability. However, setting up Docker Apache httpd may require initial learning about Docker concepts.(httpd - Official Image | Docker Hub. (n.d.). https://hub.docker.com/_/httpd ).
Flask is a web framework for Python that facilitates communication between software applications over the internet. It provides tools and principles for designing web services, enabling developers to build and manage web applications and APIs efficiently. Flask operates on the basis of URLs, identifying different resources and employing standard HTTP methods for performing operations on these resources. The framework follows an architectural style, Representational State Transfer (REST), emphasizing statelessness in client-server interactions. By adhering to REST principles, Flask simplifies server design and enhances scalability. With its ease of use and seamless integration with Python, Flask has become a popular choice among developers for building web applications and APIs, supporting diverse projects in web development and beyond.
Overall, Flask's user-friendly interface, lightweight structure, and seamless Python integration make it an excellent choice for developers looking to build efficient and scalable web applications. Its philosophy of simplicity and the ability to adapt to various project sizes and requirements have contributed to its popularity and position as one of the leading web frameworks in the Python ecosystem.

### **Python Scapy**

Python Scapy is a powerful packet manipulation library for Python, serving as a fundamental tool for network analysis and security tasks. It equips users to explore and interact with network packets, enabling developers to create, modify, and send packets across a network while capturing and analyzing network traffic. Scapy supports many protocols and packet types, facilitating seamless work with networking technologies such as Ethernet, IP, TCP, UDP, DNS, ARP, and more. Its flexible and interactive shell empowers users to craft custom packets and observe real-time network traffic, allowing for network simulation, performance analysis, and troubleshooting. A key advantage of Scapy lies in its ability to operate at a low level, providing granular control over individual packets. This feature makes it particularly valuable to network engineers, security professionals, and anyone seeking to understand and manipulate network traffic in a precise manner.
Python Scapy is a valuable asset for network exploration and manipulation, offering a comprehensive toolkit for tackling network analysis and security challenges. Its versatility and low-level control capabilities position it as a crucial resource for professionals in the networking domain, enabling them to interact with network packets effectively and gain valuable insights into network operations.

### Arp spoofing 

ARP spoofing is a type of cybercrime in which the hacker sends spoofed ARP messages to link their Media Access Control address or MAC address with the target’s IP address. This way, the hacker gains access to the victim's device’s communications, including sensitive data such as passwords and credit card information.  ARP spoofing occurs when an attacker manipulates the relationship between Media Access Control (MAC) addresses and Internet Protocol (IP) addresses.  ARP spoofing attack occurs on a local area network. 
ARP spoofing is considered dangerous as it’s used to initiate attacks like DoS and session hijacking. It’s just a starting point, and like any man-in-the-middle attack, it can act as a starting point to more serious intrusions. Once the victim’s device is corrupted, the attacker steers traffic toward them, using such information for the wrong actions.
The best way to stop ARP spoofing is to use a VPN.  VPN is a technology that encrypts the internet traffic and alters your online identity for secure browsing.

### HTTP sniffing 

A technique used to record and examine HTTP communication between a client, such as a web browser and a web server, is known as HTTP sniffing, also known as HTTP traffic sniffing or packet sniffing. This kind of cyberattack involves the interception and inspection of data packets traveling over the network by an attacker in order to retrieve sensitive data such as login passwords, session tokens, or other sensitive information sent in plaintext. The attacker could obtain unauthorized access to sensitive information by listening in on unencrypted HTTP traffic using tools like packet sniffers or network analyzers. Web applications should use secure communication protocols like HTTPS, which encrypt data during transmission, making it more difficult for attackers to capture and decrypt sensitive data to guard against HTTP sniffing attacks. 

### Reverse shell (Netcat)

In network security and penetration testing, a reverse shell is a potent tool for gaining remote access to and control over a compromised system. Instead of the usual technique, when the attacker connects directly to the target, it involves the construction of an interface from the target system to an attacker-controlled machine. Due to its ease of use and accessibility, Netcat, sometimes known as "NC," is a flexible command-line utility that is frequently used to build reverse shells. On the attacker's computer, a Netcat listener watches for incoming connections. The attacker afterward installs a payload on the target system, generally a shell script or malware, which establishes a connection with the Netcat listener. The attacker gains a command prompt on the target machine as soon as the connection is made, enabling them to execute various commands and perform malicious activities remotely. 
Netcat, frequently referred to as "NC," is a flexible networking tool that can be found in many different operating systems. It can read and write data throughout network connections and functions utilizing both the TCP and UDP protocols.  It is a sophisticated tool for file transfers and managing networks and a simple network scanner, port listener, and chat server. Netcat is frequently used in security audits and penetration tests to develop backdoors and create reverse shells on compromised systems. 


## Code developed for project 


### app.py
This Python code sets up a basic Flask web application, functioning as a searchable database of book titles. Additionally, it contains an intentional vulnerability for demonstration purposes. Let's walk through how to use it.
The application, when launched, initiates a Flask server on the IP address '0.0.0.0', listening on port '5000' on your local host.

The landing page, as denoted by the route decorator @app.route("/"), accepts both "GET" and "POST" methods. When the server receives a "GET" request, typically from a user who has just navigated to the website, it responds by rendering an HTML page using the 'index.html' template.
When the server receives a "POST" request, this is typically from a form submission on the website. The server looks for a "search" field in the form data. If it finds a value, it interprets this as a query against the database of book titles. It then calls the search_data(query) function, which scans through the 'data' list and returns any items that contain the query string in a case-insensitive manner.
If the debug mode is activated, and the query begins with 'debug:,' the application treats the subsequent text as a command to be executed on the server. It uses Python's subprocess module to run this command, captures the output, and then returns it to be displayed on the web page. This feature is designed to demonstrate a potential security vulnerability in the web application.
In a typical use case, a user would type a query into a search bar on the 'index.html' page and then submit the form. The server would then respond with a new page displaying either a list of matching book titles or the results of a command execution if the debug mode is enabled and the query started with 'debug:'

![Alt Text](https://github.com/mdjislam123/Network_Hacking/blob/main/AppPy.png)
 
### scan_network.py

This Python script leverages the Scapy module to perform a network scan, providing detailed information about all devices within a specified network range. The script is executed from the command line and requires the user to specify the network range to be scanned.
Here's how to use it:
First, you need to execute this script from the command line. You do this by typing "python scan_network.py –network 192.168.1.0/24", where `scan_network.py` is the name of this Python script file, and `192.168.1.0/24` is the range of IP addresses you want to scan. For example, `python scan_network.py –network 192.168.1.0/24` would scan all devices on the network '192.168.1.X', where 'X' is any number from 0 to 255.
The `get_arguments()` function handles the command line arguments. It sets up an ArgumentParser object, which specifies that a user should provide a network range to scan with the '-n' or '--network' option. If no network range is given, the script throws an error and stops executing.
Once the network range is parsed from the command line, the `scan(ip)` function is called. This function creates an ARP (Address Resolution Protocol) request targeted at the IP range provided by the user. The ARP request is broadcast on the network, and any responses are captured.
 
The script prints out the device's IP address and MAC address for every device that responds to the ARP request. It also attempts to resolve and print the device's hostname using Python's built-in `socket.gethostbyaddr()` function. If the hostname cannot be resolved, the script notifies the user.
Once all responses have been processed, the script prints a message indicating the scan is complete.
The last two lines of the script initiate the entire process, first calling `get_arguments()` to get the user-specified network range, then passing this range to the `scan()` function.
In summary, this script is a handy tool for understanding the devices present in a specific network range, providing detailed information about their IP and MAC addresses and hostnames when possible.

![Alt Text](https://github.com/mdjislam123/Network_Hacking/blob/main/ScanNetwork.png)

### arp_spoofing.py

The script implements ARP (Address Resolution Protocol) spoofing (or poisoning), a network attack that can intercept network traffic. This Python script leverages the Scapy library to create and send ARP packets that deceive network devices into redirecting network traffic to the attacker's device.
Let's discuss how to use it:
To run this script, type `python arp_spoofing –target 192.168.1.25 –gateway 192.168.1.1` on your command line, where `arp_spoofing` is the name of the script file, `192.168.1.25` is the IP address of the target machine you wish to spoof, and `192.168.1.1` is the IP address of the network's gateway.
The script gets the target and gateway IP addresses from the command-line arguments through the `get_arguments()` function.
Next, the `get_mac(ip)` function retrieves the MAC address of a given IP address by sending an ARP request packet. The first response received is assumed to be correct, and the MAC address is extracted and returned.
The `spoof(192.168.1.25)` function constructs an ARP packet that tells the target machine that we have the MAC address for the `spoof_ip.` Because ARP is a stateless protocol, the target machine updates its ARP cache with the MAC address in the packet—this is the MAC address of the machine running this script. This process deceives the target into sending network traffic meant for `spoof_ip` to us instead.
The `restore(192.168.1.53)` function reverses the ARP spoof by sending out ARP packets that contain the correct MAC addresses of the `source_ip` and `destination_ip.` This function is crucial for not leaving traces of the attack and for preventing network disruption when the script stops.
Once set up, the script enters a loop, continuously sending out the spoofed ARP packets to both the target and the gateway. This loop continues until the script is interrupted with a keyboard interrupt (Ctrl + C), at which point, the script restores the ARP caches on the target and gateway back to their correct states.
This script, thus, effectively performs a 'man-in-the-middle' attack by fooling the target machine into sending its traffic to the attacker's machine. It's worth noting that this kind of attack raises serious ethical and legal issues, and this explanation is for educational purposes only.

![Alt Text](https://github.com/mdjislam123/Network_Hacking/blob/main/ArpSpoofing1.png)
![Alt Text](https://github.com/mdjislam123/Network_Hacking/blob/main/ArpSpoofing2.png)

### http_sniffing.py

The Python script sniffs network packets on a given network interface and filters HTTP traffic and data load containing specific keywords, primarily used for usernames, passwords, and emails. It is a network packet sniffer implemented using the Scapy library.
To utilize this script, you would use the command: `python http_sniffing.py -interface WiFi,` where `http_sniffing.py` is the script's filename and `WiFi` is the network interface you want to monitor, like 'eth0' or 'wlan0'.
**Let's discuss the script's functions:**
1. `sniff(interface)`: This function starts the packet sniffing process on the provided network interface. The `store=False` argument ensures that Scapy does not keep packets in memory, and `prn=process_packets` sets a callback function that is executed every time a packet is captured.
2. `process_packets(packet)`: This function processes each packet the sniffer captures. It checks if the packet has TCP and Raw layers. If so, it extracts the raw load, tries to decode it using UTF-8 encoding (or 'Latin-1' if that fails), and checks if "HTTP" is present in the load. If "HTTP" is found, it means this packet contains HTTP traffic, and the function then extracts the URL using `extract_url(load).` It also checks if the load contains any predefined keywords (like "password," "user," etc.) that might indicate sensitive information.
3. `extract_url(payload)`: This function extracts the host URL from the HTTP payload. It finds the start and end of the URL within the payload and returns it.
The script also uses a list of `words` containing strings commonly used in forms, such as "username," "password," etc. When any of these words is detected in the data load of a packet, it is printed to the console.
The bottom of the script sets up command-line argument parsing and starts the sniffing process on the specified interface.

![Alt Text](https://github.com/mdjislam123/Network_Hacking/blob/main/HttpSniffing.png)
 
### net_interfaces.py

This simple Python script uses the `psutil` library to fetch network interface statistics and print the names of all network interfaces available on your machine.
`psutil` is a Python cross-platform library to access system details and process utilities. It is mainly used for system monitoring, profiling, and limiting process resources.

### Here's how the script works:

1. `nics = psutil.net_if_stats()`: This line calls the `net_if_stats` function from the `psutil` library, which returns a dictionary where keys are the network interface names, and the values are named tuples representing network interface statistics. The `net_if_stats` function provides information about each network interface card (NIC) installed on the system.
 
2. The `for` loop: This iterates over the dictionary's keys (which are the names of the network interfaces) and prints each network interface's name.
To use this script, you would need to run it in a Python environment. The output will be a list of network interface names, printed one per line. The names could be something like 'eth0', 'wlan0', 'lo,' etc., depending on the network interfaces available on your system.

![Alt Text](https://github.com/mdjislam123/Network_Hacking/blob/main/NetInterfaces.png)
