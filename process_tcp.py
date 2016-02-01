#!/usr/bin/env python
import dpkt
import socket_manager as sm
import zlib


def process_tcp():
    s_in = sm.get_and_bind_socket(5007)
    s_in.listen(1)
    conn, address = s_in.accept()
    tcp_packets = []

    while 1:
        try:
            pkt = conn.recv(sm.BUFFER_SIZE)
            if not pkt:
                conn.close()
                break
            tcp_packets.append(pkt)
        except AttributeError:
            pass

    temp_str = ''  # variable used in joining tcp.data
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
    process_tcp()
