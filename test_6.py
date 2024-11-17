from scapy.all import *
from scapy.layers.dns import DNS, DNSQR

def send_mx_query(domain, record_type):
    dns_query = IP(dst='8.8.8.8') / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname=domain, qtype=record_type))

    response = sr1(dns_query, verbose=0)

    if response:
        response.show()
    else:
        print("No response received.")

if __name__ == "__main__":
    domain = "google.com"
    record_type = 'MX'
    send_mx_query(domain, record_type)
