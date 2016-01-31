#!/usr/bin/env python
import dpkt
import socket_manager as sm


def process_tcp():
    s_in = sm.get_and_bind_socket(5007)
    s_in.listen(1)
    conn, address = s_in.accept()

    while 1:
        try:
            pkt = conn.recv(sm.BUFFER_SIZE)
            if not pkt:
                conn.close()
                break
            eth = dpkt.ethernet.Ethernet(pkt)
            ip = eth.data
            tcp = ip.data
            print tcp.sport
        except AttributeError:
            pass


if __name__ == '__main__':
    process_tcp()
