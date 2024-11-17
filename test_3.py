from scapy.all import *

qname = "example.com"
question = DNSQR(qname=qname, qtype="A")

answers = [
    DNSRR(rrname=qname, ttl=300, rdata="93.184.216.34"),
    DNSRR(rrname=qname, ttl=300, type="AAAA", rdata="2606:2800:220:1:248:1893:25c8:1946")
]

authority = [
    DNSRR(rrname=qname, ttl=172800, type="NS", rdata="ns1.example.com"),
    DNSRR(rrname=qname, ttl=172800, type="NS", rdata="ns2.example.com")
]

additional = [
    DNSRR(rrname="ns1.example.com", ttl=86400, rdata="192.0.2.1"),
    DNSRR(rrname="ns2.example.com", ttl=86400, rdata="192.0.2.2")
]

dns_pkt = DNS(id=0xC3D4, qr=1, rd=1, ra=1, qd=question, an=answers, ns=authority, ar=additional)
pkt = IP(src="192.168.1.5", dst="1.1.1.1") / UDP(sport=53, dport=54321) / dns_pkt


send(pkt)
