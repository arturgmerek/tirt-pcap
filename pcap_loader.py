#!/usr/bin/env python
import dpkt
import socket_manager as sm


def load_and_filter_tcp():
    f = open('simple.pcap', 'rb')
    p = dpkt.pcap.Reader(f)
    s = sm.get_socket()
    s.connect(sm.TCP_TUPLE)

    for ts, pkt in p:
        try:
            eth = dpkt.ethernet.Ethernet(pkt)
            ip = eth.data
            tcp = ip.data
            if tcp.sport == 80 and len(tcp.data) > 0:
                s.send(pkt)
        except AttributeError:
            pass

    s.close()
    f.close()


if __name__ == '__main__':
    load_and_filter_tcp()
