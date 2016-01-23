#!/usr/bin/env python
import dpkt
import socket_manager as sm


def process_tcp():
    s_in = sm.get_and_bind_socket(5007)
    s_in.listen(1)
    conn, address = s_in.accept()

    # s_out = sm.get_socket()
    # s_out.connect((sm.TCP_IP, 5007))

    while 1:
        pkt = conn.recv(sm.BUFFER_SIZE)
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        tcp = ip.data
        if not tcp:
            conn.close()
            break
        if type(ip.data) == dpkt.tcp.TCP:
            print(tcp)


if __name__ == '__main__':
    process_tcp()
