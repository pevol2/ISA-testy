from scapy.all import IPv6, UDP, DNS, DNSQR, send

destination_ip = "fe80::1"
destination_port = 53                  

dns_query = IPv6(dst=destination_ip)/UDP(dport=destination_port)/DNS(rd=1, qd=DNSQR(qname="example.com"))

send(dns_query)

print("DNS query sent!")
