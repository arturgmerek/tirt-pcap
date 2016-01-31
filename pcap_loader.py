#!/usr/bin/env python
import dpkt
import socket_manager as sm
import zlib


def load_and_filter_tcp():
    f = open('simple.pcap', 'rb')
    p = dpkt.pcap.Reader(f)
    s = sm.get_socket()
    s.connect(sm.TCP_TUPLE)

    tcp_packets = []
    for ts, pkt in p:
        try:
            eth = dpkt.ethernet.Ethernet(pkt)
            ip = eth.data
            tcp = ip.data
            if tcp.sport == 80 and len(tcp.data) > 0:
                s.send(pkt)
                tcp_packets.append(pkt)
        except AttributeError:
            pass

    s.close()
    f.close()

    temp_str = ''
    http_packets = []
    for p in tcp_packets:
            eth = dpkt.ethernet.Ethernet(p)
            ip = eth.data
            tcp = ip.data
            # length = len(tcp.data)
            # print ("\nThis packet's sequence number: %d" % tcp.seq)
            # print ("Next packet's sequence number: %d" % (tcp.seq + length))
            temp_str += tcp.data
            if is_push_set(tcp):
                http_packets.append(temp_str)
                temp_str = ''

    for h in http_packets:
        try:
            http = dpkt.http.Response(h)
            print http.status
            body = zlib.decompress(http.body, 16+zlib.MAX_WBITS)
            with open("Output.txt", "w") as text_file:
                text_file.write("\nHttp body: \n{0}".format(body))
        except dpkt.dpkt.UnpackError as e:
            print (e.message)
        except zlib.error as e:
            print e.message


def is_push_set(tcp):
    ack_flag = (tcp.flags & dpkt.tcp.TH_ACK) != 0
    psh_flag = (tcp.flags & dpkt.tcp.TH_PUSH) != 0
    if ack_flag and psh_flag:
        return True


if __name__ == '__main__':
    load_and_filter_tcp()
