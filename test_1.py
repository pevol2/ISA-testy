from scapy.all import IP, UDP, DNS, DNSQR, send

destination_ip = "8.8.8.8"
destination_port = 53        

dns_query = IP(dst=destination_ip)/UDP(dport=destination_port)/DNS(rd=1, qd=DNSQR(qname="example.com"))

send(dns_query)

print("DNS query sent!")
